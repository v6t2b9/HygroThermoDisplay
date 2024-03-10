from machine import I2C, Pin
from utime import sleep_ms , sleep

# Constants for the DHT20 I2C address and commands
DHT20_I2C_ADDR = 0x38  # Replace with the actual address if different

class DHT20:
    """Class to interact with the DHT20 temperature and humidity sensor."""
    def __init__(self, i2c):
        """
        Initialize the DHT20 sensor.

        Args:
            i2c: The I2C bus object used for communication.
        
        Raises:
            Exception: If the DHT20 sensor is not ready.
        """
        self.i2c = i2c
        self.address = DHT20_I2C_ADDR
        if not self.is_ready():
            raise Exception("DHT20 sensor not ready.")

    def is_ready(self):
        """
        Check if the DHT20 sensor is ready.

        Returns:
            bool: True if the sensor is ready, False otherwise.
        """
        try:
            self.i2c.writeto(self.address, bytearray([0x71]))
            status = self.i2c.readfrom(self.address, 1)
            if status[0] & 0x18 == 0x18:
                return True
            else:
                return False
                
        except OSError:
            return False

    def _trigger_measurement(self):
        """
        Trigger the sensor to perform a measurement.
        """
        self.i2c.writeto(self.address, bytearray([0xAC, 0x33, 0x00]))
        sleep_ms(100)

    def get_measurements(self):
        """
        Get temperature and humidity measurements.

        Returns:
            tuple: A tuple containing the temperature and humidity values.
        """
        self._trigger_measurement()
        data = self.i2c.readfrom(self.address, 7)
        s_rh = data[1] << 12 | data[2] << 4 | data[3] >> 4
        s_t = ((data[3] & 0x0F) << 16) | data[4] << 8 | data[5]
        humidity = (s_rh / 2**20) * 100
        temperature = (s_t / 2**20) * 200 - 50
        return temperature, humidity

    def debug_raw_data(self):
        """
        Debug function to print raw data.
        """
        self._trigger_measurement()
        raw_data = self.i2c.readfrom(self.address, 7)
        print("Raw data:", raw_data)

'''
# only if main.py is executed
if __name__ == "__main__":

    # Initialize I2C to the pins you're using
    i2c = I2C(0, scl=Pin(1), sda=Pin(0))

    # Create a DHT20 instance
    sensor = DHT20(i2c)

    # perform measurements every 5 seconds while the sensor is ready
    while sensor.is_ready():
        temperature, humidity = sensor.get_measurements()
        print(f"Temperatur: {temperature:.2f}°C, Luftfeuchtigkeit: {humidity:.2f}%")
        sleep(2)

    print("Sensor ist nicht bereit.")
'''

