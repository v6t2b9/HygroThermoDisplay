# README für das Raspberry Pi Pico WH Temperatur- und Feuchtigkeitsmessprojekt

Mit diesem Projekt kann ein Raspberry Pi Pico WH Temperatur- und Feuchtigkeitsmessungen mit dem DHT20-Sensor durchführen und auf einem LCD-Display anzeigen.

## Voraussetzungen

- Raspberry Pi Pico WH
- DHT20 Temperatur- und Feuchtigkeitssensor
- I2C 16x2 LCD-Display
- 8 Kabel (z.B. 2x rot, 2x schwarz, 2x grün, 2x gelb)

# Verkabelung des DHT20-Sensors und des LCD-Displays mit dem Raspberry Pi Pico WH

## DHT20-Sensor
- VCC des DHT20 (linker Pin) an 3.3V (oder 5V, falls unterstützt) des Raspberry Pi Pico WH anschließen
- GND des DHT20 (2. Pin von links) an einen GND-Pin des Raspberry Pi Pico WH anschließen
- SDA des DHT20 (3. Pin von links) an Pin 0 (GPIO0) des Raspberry Pi Pico WH anschließen
- SCL des DHT20 (rechter Pin) an Pin 1 (GPIO1) des Raspberry Pi Pico WH anschließen

## I2C-LCD-Display
- VCC des Displays an 5V des Raspberry Pi Pico WH anschließen
- GND des Displays an einen GND-Pin des Raspberry Pi Pico WH anschließen
- SDA des Displays an Pin 0 (GPIO0) des Raspberry Pi Pico WH anschließen (gemeinsam mit SDA des DHT20)
- SCL des Displays an Pin 1 (GPIO1) des Raspberry Pi Pico WH anschließen (gemeinsam mit SCL des DHT20)