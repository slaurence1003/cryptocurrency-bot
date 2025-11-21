import requests
import datetime

def get_crypto_price():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data['USD']
        return price
    else:
        return None

price = get_crypto_price()
if price:
    print(f"The current price of Bitcoin is: ${price}")


def get_crypto_price_date(symbol, date_str):
    parts = date_str.split(' ')
    date_parts = parts[0].split('-')
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    time_parts = parts[1].split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1])

    dt = datetime.datetime(year, month, day, hour, minute)
    timestamp = dt.timestamp()
    
    url = f"https://min-api.cryptocompare.com/data/pricehistorical?fsym={symbol}&tsyms=USD&ts={timestamp}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data[symbol]['USD']
        return price
    else:
        return None


price_on_date = get_crypto_price_date("BTC", 2022, 1, 1)
if price_on_date:
    print(f"The price of Bitcoin on the given date was: ${price_on_date}")

user = input("Enter cryptocurrency symbol (e.g., BTC, ETH): ").upper()
user_date = input("Enter date and time (YYYY-MM-DD HH:MM): ")


