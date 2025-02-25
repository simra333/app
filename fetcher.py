import requests
from config import *

def fetch_joke(number=5):
    """Fetches a joke from the API"""
    response = requests.get(f"{JOKE_API_URL}?count={number}")

    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching joke!")
        return None

