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


def main():
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT

    ptSensor = sensors.BMP280()
    radio1Sensor = sensors.Radio(radioType=1)
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

        radio1Sensor.send(data.encode("ascii"))

        print("SENT")

        led.value = not led.value
        iteration += 1


if __name__ == "__main__":
    main()
