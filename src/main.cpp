#include <Arduino.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BME280.h>

#define BME_SCK (13)
#define BME_MISO (12)
#define BME_MOSI (11)
#define BME_CS (10)

Adafruit_BME280 bme;
Adafruit_Sensor *bme_temp = bme.getTemperatureSensor();

void setup()
{
  Serial.begin(9600);
  unsigned status;
  status = bme.begin(0x76);
  if (!status)
  {
    Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
    Serial.print("SensorID was: 0x");
    Serial.println(bme.sensorID(), 16);
    Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
    Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
    Serial.print("        ID of 0x60 represents a BME 280.\n");
    Serial.print("        ID of 0x61 represents a BME 680.\n");
    while (1)
      delay(10);
  }
}

void loop()
{
  Serial.print(F("Temperatura: "));
  Serial.print(bme.readTemperature());
  Serial.print(" *C");
  Serial.println();

  Serial.print("Cisnienie = ");
  Serial.print(bme.readPressure() / 100.0F);
  Serial.println(" hPa");

  Serial.print("Szacowana wysokosc (m. n. p. m.) = ");
  Serial.print(bme.readAltitude(1013.25));
  Serial.println(" m");

  Serial.print("Wilgotnosc = ");
  Serial.print(bme.readHumidity());
  Serial.println(" %");

  delay(5000);
}
