import httpx
import time as t
import subprocess

API_KEY = "2585c124a044449cbdceb27e3eabf860697d687c496968cdc169b889795b5393"
URL = "https://api.farenus.net/weather/stations/bierun/measurements"
HEADERS = {"X-API-Key" : API_KEY}

r = httpx.get(URL, headers=HEADERS)
data = r.json()

while True:
    for i, j in enumerate(data):
        if i > 0:
            break
        print(f"Temperatura: {j["temperature"]}")
        print(f"Wilgotnosc: {j["humidity"]}")
        print(f"Cisnienie: {j["pressure"]}")
    t.sleep(10)
    subprocess.run("clear")
    