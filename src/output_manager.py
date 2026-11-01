#import serial as s
import httpx
import time as t
import random
import os

API_KEY = "2585c124a044449cbdceb27e3eabf860697d687c496968cdc169b889795b5393"
URL = "https://api.farenus.net/weather/stations/bierun/measurements"


"""
sr = s.Serial("COM5", 9600)
if sr.is_open is False:
    try:
        sr.open()
    except s.SerialException as e:
        print(e)


temperatura = "-"
cisnienie = "-"
wilgotnosc = "-"
wysokosc = "-"


def getData():
    global temperatura, cisnienie, wilgotnosc, wysokosc
    if sr.in_waiting > 0:
        raw = sr.readline()
        clean = raw.decode("utf-8", errors="ignore").strip()
        clean = clean.replace("*C", "°C")

        if "°C" in clean:
            temperatura = clean
        elif "hPa" in clean:
            cisnienie = clean
        elif "%" in clean:
            wilgotnosc = clean
        elif "Szacowana" in clean:
            wysokosc = clean


while sr.is_open:
    getData()
    os.system("cls" if os.name == "nt" else "clear")
    print(temperatura)
    print(cisnienie)
    print(wilgotnosc)
    print(wysokosc)
    t.sleep(1)
"""

#0 -> temp 1 -> pres 2 -> humi
def send_data():
    headers = {"X-API-Key" : API_KEY, "Content-Type" : "application/json"}
    vars = [0, 0, 0]
    keys = ["temperature", "humidity", "pressure"]
    data = {}
    random_val = random.Random()
    for i, j in zip(keys, vars):
        j = 1.0*random_val.randint(1, 100)
        data.update({i : j})
        print(data[i])
    while True:
        r = httpx.post(URL, headers=headers, json=data)
        print(r.text)
        t.sleep(10)
        

send_data()