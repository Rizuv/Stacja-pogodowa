import serial as s
import time as t
import os

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
