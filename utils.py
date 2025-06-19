import requests
import secrets

def refresh_access_token():
    url = "https://www.googleapis.com/oauth2/v4/token"

    params = {
        "client_id": secrets.client_id,
        "client_secret": secrets.client_secret,
        "refresh_token": secrets.refresh_token,
        "grant_type": "refresh_token"
    }

    response = requests.post(url, data=params)
    return response.json()["access_token"]

def get_traits():
    url = f"https://smartdevicemanagement.googleapis.com/v1/enterprises/{secrets.project_id}/devices/{secrets.device_id}"

    headers = {
        "Authorization": f"Bearer {refresh_access_token()}"
    }

    response = requests.get(url, headers=headers)

    return response.json()["traits"]
