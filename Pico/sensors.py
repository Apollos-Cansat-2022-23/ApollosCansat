import adafruit_rfm9x
import board
import digitalio

import deviceCommunication
import adafruit_bmp280
import adafruit_lis3dh

class BMP280:
    def __init__(self):
        self.i2c = deviceCommunication.GetI2C()

        self.i2c.try_lock()
        print("Scan: ", self.i2c.scan())
        self.i2c.unlock()

        successful = False
        i = 0

        while not successful:
            try:
                self.sensor = adafruit_bmp280.Adafruit_BMP280_I2C(self.i2c, address=0x76)
                successful = True
            except ValueError:
                i += 1
                if i % 100 == 0:
                    print("'bmp280' not detected")

    def read(self):
        try:
            temperature, pressure = self.sensor.temperature, self.sensor.pressure

        except OSError:
            temperature, pressure = -1, -1

        return temperature, pressure


class Radio:
    def __init__(self, radioType: int):
        locationsCsReset = {
            1: [board.GP6, board.GP7],
            2: [board.GP8, board.GP9]
        }

        csLocation, resetLocation = locationsCsReset[radioType]
        cs = digitalio.DigitalInOut(csLocation)
        reset = digitalio.DigitalInOut(resetLocation)

        successful = False
        i = 0

        while not successful:
            try:
                self.rfm9x = adafruit_rfm9x.RFM9x(deviceCommunication.GetSPI(), cs, reset, 433)
                successful = True
            except RuntimeError:
                i += 1
                if i % 100 == 0:
                    print(f"'rfm9x-{radioType}' not detected")

        print(f"RFM9x {radioType} radio ready")

    def read(self, timeout=1):
        return self.rfm9x.receive(timeout=timeout)

    def send(self, message):
        self.rfm9x.send(message)


class Accelerometer:
    def __init__(self):
        self.i2c = deviceCommunication.GetI2C()

        successful = False
        i = 0

        while not successful:
            try:
                self.lis3dh = adafruit_lis3dh.LIS3DH_I2C(self.i2c)
                successful = True
            except ValueError:
                i += 1
                if i % 100 == 0:
                    print("'lis3dh' not detected")

    def read(self):
        return [
            value / adafruit_lis3dh.STANDARD_GRAVITY for value in self.lis3dh.acceleration
        ]