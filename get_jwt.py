#!/usr/bin/env python

from datetime import datetime, timedelta, timezone

from jwt import JWT, jwk_from_pem

from jwt.utils import get_int_from_datetime

from dotenv import load_dotenv

from requests import (
    get as rget,
    post
)

from os import getenv

load_dotenv()

# generate a JWT from the GitHub app private key to then be used for further authentication
instance = JWT()

payload = {
    "iat": get_int_from_datetime(datetime.now(timezone.utc)),
    "exp": get_int_from_datetime(datetime.now(timezone.utc) + timedelta(minutes=10)),
    "iss": getenv("APP_ID"),
}

with open(getenv("PEM_FILE_PATH"), "rb") as ak:
    signing_key = jwk_from_pem(ak.read())

jws = instance.encode(payload, signing_key, alg="RS256")

# Use the JWT to request an access token from the app installation
token_headers = {
    "Authorization": f"Bearer {jws}",
    "Accept": "application/vnd.github.v3+json"
}

token_request = post(f"https://api.github.com/app/installations/{getenv('APP_INSTALLATION_ID')}/access_tokens", headers=token_headers)

token = token_request.json().get("token")

api_headers = {
    "Authorization": f"token {token}"
}

private_info = rget(getenv("PRIVATE_URL"), headers=api_headers)

print(private_info.text)