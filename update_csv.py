
import requests
import csv

# Pobierz dane z CoinGecko
prices = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd").json()
global_data = requests.get("https://api.coingecko.com/api/v3/global").json()

btc_price = prices["bitcoin"]["usd"]
eth_price = prices["ethereum"]["usd"]
btc_dominance = global_data["data"]["market_cap_percentage"]["btc"]

# Zapisz dane do banana_data.csv
with open("banana_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["symbol", "value"])
    writer.writerow(["BTC_USD", btc_price])
    writer.writerow(["ETH_USD", eth_price])
    writer.writerow(["BTC_Dominance", round(btc_dominance, 2)])
