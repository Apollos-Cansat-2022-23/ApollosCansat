import digitalio
import board
import analogio
from time import sleep
import sensors


def main():
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT

    ptSensor = sensors.BMP280()
    radio1Sensor = sensors.Radio(radioType=1)
    radio2Sensor = sensors.Radio(radioType=2)
    accelerometer = sensors.Accelerometer()

    adc = analogio.AnalogIn(board.A1)

    while True:
        sleep(0.02)
        print(ptSensor.read())
        radio1Sensor.send(b"Testing")
        print(radio2Sensor.read())
        print(accelerometer.read())
        moistVal = adc.value
        percent = 2.718282 * 2.718282 * (0.008985 * moistVal + 0.207762) / 4531 * 100
        print((percent,))

        led.value = not led.value


if __name__ == "__main__":
    adc = analogio.AnalogIn(board.A1)

    while True:
        #print(((adc.value * 3.3)/65536,))
        moistVal = adc.value
        percent = 2.718282 * 2.718282 * (0.008985 * moistVal + 0.207762) / 4531 * 100
        print((percent,))
        sleep(0.1)

    main()
