import digitalio
import board
import analogio
from time import sleep

import sensors


def main():
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT

    radio1Sensor = sensors.Radio(radioType=1)
    packetCount = 0

    while True:
        sleep(0.2)
        led.value = not led.value

        #radio1Sensor.send(f"Testing {packetCount}".encode("utf-8"))
        readRadio = radio1Sensor.read(timeout=1)

        try:
            readDecode = readRadio.decode("ascii") if readRadio is not None else readRadio
            if packetCount == 50:
                raise UnicodeError("Test Error")
        except UnicodeError as e:
            print("[ERROR]", readRadio, repr(e))
        #readRadio = bytearray(b"Testing")
        print("[MSG]", packetCount, readDecode, radio1Sensor.rfm9x.rssi)
        packetCount += 1


if __name__ == "__main__":
    main()
