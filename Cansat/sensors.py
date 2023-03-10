import os

import adafruit_lis3dh
import adafruit_rfm9x
import adafruit_dht
import board
import digitalio
import analogio

import deviceCommunication
import adafruit_bmp280
import adafruit_lis3dh
import adafruit_sdcard
import storage


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
            temperature, pressure, altitude = self.sensor.temperature, self.sensor.pressure, self.sensor.altitude

        except:
            temperature, pressure, altitude = -1, -1, -1

        return temperature, pressure, altitude


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

        self.lis3dh.range = 3

    def read(self):
        try:
            return [
                value / adafruit_lis3dh.STANDARD_GRAVITY for value in self.lis3dh.acceleration
            ]

        except:
            return [-1, -1, -1]


class DHT11:
    def __init__(self):
        self.sensor = adafruit_dht.DHT11(board.GP8)

    def read(self):
        try:
            temperature, humidity = self.sensor.temperature, self.sensor.humidity

        except:
            temperature, humidity = -1, -1

        return temperature, humidity


class MQ7:
    def __init__(self):
        self.MQ7adc = analogio.AnalogIn(board.A1)
        self.MQ7In = digitalio.DigitalInOut(board.GP9)
        self.MQ7In.direction = digitalio.Direction.INPUT

    def read(self):
        return int(self.MQ7In.value), self.MQ7adc.value * 3.3 / 65535


class O2:
    def __init__(self):
        self.O2adc = analogio.AnalogIn(board.A0)

    def read(self):
        return (1 - self.O2adc.value/65535) * 25


class SD:
    def __init__(self):
        spi = deviceCommunication.GetSPI()
        cs = digitalio.DigitalInOut(board.GP10)
        sdcard = adafruit_sdcard.SDCard(spi, cs)
        vfs = storage.VfsFat(sdcard)
        storage.mount(vfs, "/sd")
        print("SD Card Ready")

        '''with open("/sd/17.txt", "r") as f:
            for line in f.readlines():
                print(line)
        '''

        for file in os.listdir("/sd"):
            if "id.txt" in file:
                break
        else:
            with open("/sd/id.txt", "w+") as f:
                f.write("0")

        self.id = 0
        # Can Error and if error, I will know.
        with open("/sd/id.txt", "r") as f:
            self.id = int(f.readline().strip()) + 1
            with open("/sd/id.txt", "w+") as f2:
                f2.write(str(self.id))
            print(f"Id is {self.id}")

        #self.file = open(f"/sd/{id}.txt", "a+")

    def write(self, content):
        with open(f"/sd/{self.id}.txt", "a+") as f:
            f.write(content + "\n")

    def __del__(self):
        self.file.close()
