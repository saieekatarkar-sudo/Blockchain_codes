"""
Week 3: Data & APIs
Description:
Fetches real-time Bitcoin price data from a public API
and demonstrates JSON parsing and error handling.
"""

import requests

API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def fetch_bitcoin_price():
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data["bpi"]["USD"]["rate"]

def main():
    try:
        price = fetch_bitcoin_price()
        print(f"Current Bitcoin Price (USD): {price}")
    except requests.exceptions.RequestException as error:
        print("Error fetching Bitcoin price.")
        print(error)

if __name__ == "__main__":
    main()
