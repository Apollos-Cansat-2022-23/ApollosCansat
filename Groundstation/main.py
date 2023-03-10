import digitalio
import board
import analogio
from time import sleep

import sensors
import EasyCrypt


def main():
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT

    radio1Sensor = sensors.Radio(radioType=1)
    packetCount = 0

    keystring = b"14789d1c3101e101f5237e2f61df5cc5"
    ivstring = "f6aef1d8b77c1503c6db373ba8331157"

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
        try:
            print("[MSG]", packetCount, EasyCrypt.decrypt_string(keystring, readDecode, ivstring) if readRadio else None, radio1Sensor.rfm9x.rssi)
        except:
            print("[MSG-ERROR]", packetCount, None, radio1Sensor.rfm9x.rssi)
        packetCount += 1


if __name__ == "__main__":
    main()
