import os
import httpx
from dotenv import load_dotenv

load_dotenv()
BASE = "https://api-m.sandbox.paypal.com"

def get_token():
    r = httpx.post(
        BASE + "/v1/oauth2/token",
        auth=(os.getenv("PAYPAL_CLIENT_ID"), os.getenv("PAYPAL_SECRET")),
        data={"grant_type": "client_credentials"},
         )
    r.raise_for_status()
    return r.json()["access_token"]