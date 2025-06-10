import requests
import csv
from datetime import datetime, timedelta

# Oblicz daty
today = datetime.utcnow().date()
yesterday = today - timedelta(days=1)

# Pobierz dane z DefiLlama API (wolumen DEX)
url = "https://api.llama.fi/overview/dexs?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true"
response = requests.get(url)
data = response.json()

# Wyciągnij wolumen DEX dla dzisiaj i wczoraj
try:
    today_volume = data['total24h']
    yesterday_volume = data['total48h'] - today_volume
    delta = (today_volume - yesterday_volume) / yesterday_volume
except Exception:
    delta = 0.0  # fallback w razie błędu

# Dopisz/aktualizuj dane do pliku CSV
rows = []
with open("banana_data.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

# Nadpisz lub dopisz wiersz z DEX_VOL_DELTA
updated = False
for row in rows:
    if row[0] == "DEX_VOL_DELTA":
        row[1] = round(delta, 4)
        updated = True
if not updated:
    rows.append(["DEX_VOL_DELTA", round(delta, 4)])

# Zapisz zaktualizowany plik
with open("banana_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
