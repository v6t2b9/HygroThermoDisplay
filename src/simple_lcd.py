# simple_lcd.py

from machine import I2C, Pin
from time import sleep
from src.machine_i2c_lcd import I2cLcd

class SimpleLCD:
    def __init__(self, i2c_channel=0, sda_pin=20, scl_pin=21, i2c_address=0x3f, lcd_columns=16, lcd_rows=2):
        self.i2c = I2C(i2c_channel, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)
        self.lcd = I2cLcd(self.i2c, i2c_address, lcd_rows, lcd_columns)

    def display_message(self, message, row=0, col=0, clear_before=False, sleep_after=0):
        if clear_before:
            self.lcd.clear()
        self.lcd.move_to(col, row)
        self.lcd.putstr(message)
        if sleep_after > 0:
            sleep(sleep_after)

    def clear(self):
        self.lcd.clear()
        
    def clear_row(self, row):
        """Löscht eine spezifische Zeile im Display."""
        self.lcd.move_to(0, row)
        self.lcd.putstr(' ' * self.lcd.num_columns)

    def display_scrolling_text(self, message, row, delay=0.3, repeat=False):
        original_message = message
        if len(message) <= self.lcd.num_columns:
            self.display_message(message, row=row)
            sleep(delay)
        else:
            padded_message = message + ' ' * self.lcd.num_columns  # Füge Leerzeichen am Ende für besseren Effekt hinzu
            while True:
                for i in range(len(padded_message) - self.lcd.num_columns + 1):
                    self.clear_row(row)
                    self.display_message(padded_message[i:i+self.lcd.num_columns], row=row, clear_before=False)
                    sleep(delay)
                if not repeat:
                    break
                message = padded_message + original_message  # Reset message for repeat


'''
# main.py

from src.simple_lcd import SimpleLCD

# Erstelle ein SimpleLCD Objekt
lcd = SimpleLCD(i2c_address=0x3f, lcd_columns=16, lcd_rows=2)

# Anzeigen eines festen Textes in der unteren Zeile
lcd.display_message('YYY', row=1, col=0)

# Laufschrift für die obere Zeile
lcd.display_scrolling_text('Laufschrift oben - laenger als 16 Zeichen', row=0, delay=0.4, repeat=True)

# Optional: Warte und lösche den Bildschirm
# sleep(10)
# lcd.clear()
'''
