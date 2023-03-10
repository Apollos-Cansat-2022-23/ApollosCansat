import time

import digitalio
import board
import analogio
from time import sleep
import sensors
import json
import math
import deviceCommunication
import aesio
import EasyCrypt


def main():
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT

    sd = sensors.SD()
    ptSensor = sensors.BMP280()
    radio1Sensor = sensors.Radio(radioType=1)
    #radio2Sensor = sensors.Radio(radioType=2)
    accelerometer = sensors.Accelerometer()

    dht11 = sensors.DHT11()
    mq7 = sensors.MQ7()
    o2 = sensors.O2()

    adc = analogio.AnalogIn(board.A2)
    iteration = 0

    ptSensor.sensor.sea_level_pressure = 1013.25
    initTemp, initPressure, _ = ptSensor.read()
    initTemp += 273.15
    initPressure *= 0.1

    key = b'Sixteen byte key'
    cipher = aesio.AES(key, aesio.MODE_CBC)

    print("Files on filesystem:")
    print("====================")
    #deviceCommunication.print_directory("/sd", tabs=4)
    print("====================")

    keystring = b"14789d1c3101e101f5237e2f61df5cc5"
    ivstring = "f6aef1d8b77c1503c6db373ba8331157"

    while True:
        sleep(0.2)

        data = {}

        temperature, pressure, altitude = ptSensor.read()

        accelX, accelY, accelZ = accelerometer.read()
        moistVal = adc.value
        percent = 2.718282 * 2.718282 * (0.008985 * moistVal + 0.207762) / 4531 * 100

        temperature2, humidity = dht11.read()
        gasLeakage, gasValue = mq7.read()

        oxygen = o2.read()

        print("Sending....", end=" ")
        data = f"[APOLLOS] {pressure} {temperature} {accelX} {accelY} {accelZ} {altitude} {temperature2} {humidity} {gasLeakage} {gasValue} {oxygen} {percent} {time.monotonic_ns()} {iteration}"
        sd.write(data)

        inpstring = data

        crypted = EasyCrypt.encrypt_string(keystring, inpstring, ivstring)
        radio1Sensor.send(crypted)
        #radio1Sensor.send(b"Testing")
        print("SENT")
        print(data)

        led.value = not led.value
        iteration += 1


if __name__ == "__main__":
    """key = b'Sixteen byte key'
    inp = 'CircuitPython!!!'.encode("ascii")  # Note: 16-bytes long
    outp = bytearray(len(inp))
    outp2 = bytearray(len(inp))

    cipher = aesio.AES(key, aesio.MODE_CBC)
    cipher.encrypt_into(inp, outp)
    print(key)
    print(outp)
    cipher.decrypt_into(outp, outp2)
    print(outp2)"""
    main()
