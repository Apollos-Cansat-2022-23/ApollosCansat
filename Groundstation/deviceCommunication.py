import board
import busio

cache = {}


def GetSPI():
    if "spi" not in cache:
        spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)
        cache["spi"] = spi

    return cache["spi"]
