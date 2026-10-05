Projekt Stacja Pogodowa:
---------
**BME280**
-> Odpowiada za zbieranie danych z otoczenia (temperatura, wiglotnosc, cisnienie)
-> Sensor BME280 jest podlaczone w obwodznie do Arduino, piny input zbieraja dane w postaci napiecie na danych pinach
-> Biblioteka *Adafruit_BME280* przetwarze napiecie na odpowiednie odczyty
**Program C++ na Arduino**
-> Przetwarza dane odczytu i modyfikuje je do postaci wysylanej przez Serial
**Program Python na innym urzadzeniu**
-> Urzadzenie podpiete pod Serial odbiera odpowiednio przygotowane dane
-> output_manager.py przy uzyciu biblioteki Serial ma za zadanie przedstawic uzytkownikowi dane w odpowiednim formacie (tutaj na terminalu)

*Program ma potencjal na rozszerzanie go o werstwe wizualna GUI, lub podpiecie systemow analizy danych pogodowych*
