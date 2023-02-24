import time

import digitalio
import board
import analogio
from time import sleep
import sensors
import json
import math
import adafruit_dht
import deviceCommunication


def main():
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT

    ptSensor = sensors.BMP280()
    radio1Sensor = sensors.Radio(radioType=1)
    #radio2Sensor = sensors.Radio(radioType=2)
    accelerometer = sensors.Accelerometer()

    #dht = adafruit_dht.DHT11(board.GP8)

    MQ135adc = analogio.AnalogIn(board.A2)
    MQ135In = digitalio.DigitalInOut(board.GP22)
    MQ135In.direction = digitalio.Direction.INPUT


    #adc = analogio.AnalogIn(board.A1)
    iteration = 0

    ptSensor.sensor.sea_level_pressure = 1013.25
    initTemp, initPressure, _ = ptSensor.read()
    initTemp += 273.15
    initPressure *= 0.1
    print(accelerometer.lis3dh.data_rate, accelerometer.lis3dh.range)
    while True:
        sleep(0.2)

        data = {}

        temperature, pressure, altitude = ptSensor.read()
        data["temperature"] = temperature
        data["pressure"] = pressure
        data["altitude"] = altitude
        #print(temperature)
        H = 1.38 * pow(10, -23) * ((initTemp + 273.15 - (temperature + 273.15)) / 2) / (471.6671544 * pow(10, -27))
        h = -H*math.log(pressure*0.1 / initPressure)

        data["h"] = h
        #print(radio2Sensor.read())
        #print(accelerometer.read())

        #data["accelerationX"], data["accelerationY"], data["accelerationZ"] = accelerometer.read()
        accelX, accelY, accelZ = accelerometer.read()
        #moistVal = adc.value
        #percent = 2.718282 * 2.718282 * (0.008985 * moistVal + 0.207762) / 4531 * 100
        #print((percent,))

        print("Sending....", end=" ")
        data = f"[APOLLOS] {pressure} {temperature} {accelX} {accelY} {accelZ} {altitude} {time.monotonic_ns()} {iteration}"
        radio1Sensor.send(data.encode("ascii"))
        #radio1Sensor.send(b"Testing")
        print("Sent")
        print(data)

        print("MQ135", MQ135In.value, MQ135adc.value)

        #print(dht.temperature, dht.humidity)

        led.value = not led.value
        iteration += 1


if __name__ == "__main__":
    #adc = analogio.AnalogIn(board.A1)
    """
    while True:
        #print(((adc.value * 3.3)/65536,))
        moistVal = adc.value
        percent = 2.718282 * 2.718282 * (0.008985 * moistVal + 0.207762) / 4531 * 100
        print((percent,))
        sleep(0.1)"""

    #led = digitalio.DigitalInOut(board.GP25)
    #led.direction = digitalio.Direction.OUTPUT
    #led.value = True

    """
    i2c = deviceCommunication.GetI2C()

    i2c.try_lock()
    print("Scan: ", i2c.scan())
    i2c.unlock()"""
    #import busio
    #uart = busio.UART(board.GP16, board.GP17, baudrate=9600)

    """while True:
        data = uart.read(2)  # read up to 32 bytes
        print(data)  # this is a bytearray type

        if data is not None:
            led.value = True

            # convert bytearray to string
            data_string = ''.join([chr(b) for b in data])
            print(data_string, end="")

            led.value = False"""
    """import test
    oxygen = test.DFRobot_Oxygen_IIC(0x01, 0x74)
    adc = analogio.AnalogIn(board.A0)

    while True:
        oxygen_data = oxygen.get_oxygen_data(10)
        print("oxygen concentration is %4.2f %%vol" % oxygen_data, (1 - adc.value/65535) * 25)
        time.sleep(1)
    OXYGEN_CONECTRATION = 20.9  # The current concentration of oxygen in the air.
    OXYGEN_MV = 0  # The value marked on the sensor, Do not use must be assigned to 0."""


    """def setup():
        '''
          The first  parameter is to select iic0 or iic1
          The second parameter is the iic device address
          The default address for iic is ADDRESS_3
          ADDRESS_0                 = 0x70
          ADDRESS_1                 = 0x71
          ADDRESS_2                 = 0x72
          ADDRESS_3                 = 0x73
        '''
        oxygen = test.DFRobot_Oxygen_IIC(0x01, 0x74)
        oxygen.calibrate(OXYGEN_CONECTRATION, OXYGEN_MV)
        print("oxygen calibrate success")
        time.sleep(1)
    setup()"""
    main()
