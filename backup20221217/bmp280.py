# Write your code here :-)
import board
import busio
import adafruit_bmp280

def setup(i2c):
    i2c.try_lock()
    print("Scan: ", i2c.scan())
    i2c.unlock()

    bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

    return bmp280_sensor

def read_data(sensor):
    return sensor.temperature, sensor.pressure



