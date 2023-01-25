import digitalio
import analogio
import board
import time
import busio

cache = {}

# TODO: Memoiziation
def GetI2C():
    if "i2c" not in cache:
        i2c = busio.I2C(scl=board.GP15, sda=board.GP14)
        cache["i2c"] = i2c

    return cache["i2c"]


def GetSPI():
    if "spi" not in cache:
        spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
        cache["spi"] = spi

    return cache["spi"]
