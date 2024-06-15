import requests

API_KEY = 'fca_live_tEfxqyi0hiubfqNifiKaFXt1ZclXQsmU9SYTPumW'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    
    except Exception as e:
        print("Invalid currency!")
        return None


while True:
    base = input("Enter currency to convert:     X = QUIT").upper()

    if base == "X":
        break

    data = convert_currency(base)

    if not data:
        continue

    for ticker, value in data.items():
        print(f"{ticker}: {value}")
