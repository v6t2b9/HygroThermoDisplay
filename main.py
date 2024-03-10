from machine import I2C, Pin
from utime import sleep
from src.DHT20 import DHT20
from src.simple_lcd import SimpleLCD

# Initialisiere I2C an den Pins, die für Ihr Setup verwendet werden
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Beispiel: Verwenden Sie die korrekten Pins für Ihren Aufbau

# Erstelle Sensor- und Display-Objekte
sensor = DHT20(i2c)
lcd = SimpleLCD(i2c_channel=0, sda_pin=0, scl_pin=1, i2c_address=0x3f, lcd_columns=16, lcd_rows=2)

#lcd.backlight_on()

while True:
    if sensor.is_ready():
        temperature, humidity = sensor.get_measurements()
        lcd.display_message(f'Temperatur: {temperature:.2f}C', 0, 0, clear_before=True)
        lcd.display_message(f'Feuchte:  {humidity:.2f}%', 1, 0)
    else:
        lcd.display_message("Sensor nicht bereit", 0, 0, clear_before=True)
    
    sleep(5)  # Warte 5 Sekunden vor der nächsten Messung
