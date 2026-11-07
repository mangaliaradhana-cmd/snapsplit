from fastapi import FastAPI
from paypal_client import get_token

app = FastAPI()


@app.get("/")
def home():
    return {"status": "SnapSplit is running"}


@app.get("/test-paypal")
def test_paypal():
    token = get_token()
    return {"paypal_connected": True, "token_start": token[:6]}