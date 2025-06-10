import requests
import csv

# Pobierz dane z DefiLlama
url = "https://api.llama.fi/overview/dexs?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true"
response = requests.get(url)
data = response.json()

# Oblicz wolumen i zmianę
try:
    today_volume = data['total24h']
    yesterday_volume = data['total48h'] - today_volume
    delta = (today_volume - yesterday_volume) / yesterday_volume
    delta = round(delta, 4)
except Exception:
    delta = 0.0

# Wczytaj istniejący plik CSV i zaktualizuj dane
rows = []
symbols = {}

try:
    with open("banana_data.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row) == 2:
                symbols[row[0]] = row[1]
except FileNotFoundError:
    header = ["symbol", "value"]

# Zaktualizuj lub dodaj DEX_VOL_DELTA
symbols["DEX_VOL_DELTA"] = delta

# Zapisz cały plik ponownie
with open("banana_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for key, value in symbols.items():
        writer.writerow([key, value])
