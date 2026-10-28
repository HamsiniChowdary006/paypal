"""Proofpay PayPal sandbox smoke test: create (AUTHORIZE) -> approve in browser -> authorize -> capture.

Setup:  pip install httpx
Run:    python sandbox_smoke.py
Needs PAYPAL_CLIENT_ID and PAYPAL_CLIENT_SECRET in the environment or a .env file (sandbox app credentials).
Put this file in scripts/ in the repo.
"""
import os
import sys
import uuid
from pathlib import Path

import httpx

BASE = "https://api-m.sandbox.paypal.com"  # sandbox only, never live


def load_env() -> None:
    env = Path(".env")
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


def get_token(client: httpx.Client) -> str:
    resp = client.post(
        f"{BASE}/v1/oauth2/token",
        auth=(os.environ["PAYPAL_CLIENT_ID"], os.environ["PAYPAL_CLIENT_SECRET"]),
        data={"grant_type": "client_credentials"},
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "PayPal-Request-Id": str(uuid.uuid4()),  # makes retries safe
    }


def main() -> None:
    load_env()
    with httpx.Client(timeout=30) as client:
        token = get_token(client)
        print("1. Got access token")

        order = client.post(
            f"{BASE}/v2/checkout/orders",
            headers=headers(token),
            json={
                "intent": "AUTHORIZE",
                "purchase_units": [{"amount": {"currency_code": "USD", "value": "5.00"}}],
                "payment_source": {
                    "paypal": {
                        "experience_context": {
                            "return_url": "https://example.com/return",
                            "cancel_url": "https://example.com/cancel",
                            "user_action": "PAY_NOW",
                        }
                    }
                },
            },
        )
        order.raise_for_status()
        data = order.json()
        order_id = data["id"]
        approve = next(
            link["href"] for link in data["links"] if link["rel"] in ("payer-action", "approve")
        )
        print(f"2. Created order {order_id}")
        print("\nOpen this link, log in with your SANDBOX PERSONAL (buyer) account, and approve:")
        print(approve)
        print("\n(After approving you'll land on example.com, that's expected. Come back here.)")
        input("\nPress Enter once you've approved... ")

        auth = client.post(
            f"{BASE}/v2/checkout/orders/{order_id}/authorize", headers=headers(token), json={}
        )
        if auth.status_code >= 400:
            print("Authorize failed:", auth.text)
            sys.exit(1)
        authorization = auth.json()["purchase_units"][0]["payments"]["authorizations"][0]
        auth_id = authorization["id"]
        print(f"3. Authorized. Authorization id {auth_id}, status {authorization['status']}")

        choice = input("Capture now (c) or void (v)? ").strip().lower()
        if choice == "v":
            void = client.post(f"{BASE}/v2/payments/authorizations/{auth_id}/void", headers=headers(token))
            print("4. Voided." if void.status_code in (200, 204) else f"Void failed: {void.text}")
        else:
            cap = client.post(
                f"{BASE}/v2/payments/authorizations/{auth_id}/capture",
                headers=headers(token),
                json={"final_capture": True},
            )
            if cap.status_code >= 400:
                print("Capture failed:", cap.text)
                sys.exit(1)
            print(f"4. Captured. Capture id {cap.json()['id']}, status {cap.json()['status']}")
        print("\nPayPal sandbox flow works.")


if __name__ == "__main__":
    main()
