# Write your code here :-)
import digitalio
import analogio
import board
import time
import radio
import bmp280
import accelermator
import busio

"""adc = analogio.AnalogIn(board.GP26)

while True:
    print(((adc.value * 3.3)/65536,))
    time.sleep(0.1)"""

i2c = busio.I2C(scl=board.GP15, sda=board.GP14)
bmp280_sensor = bmp280.setup(i2c)

accel = accelermator.setup(i2c)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True
led1 = digitalio.DigitalInOut(board.GP27)
led1.direction = digitalio.Direction.OUTPUT
led1.value = True

sleepVal = 0.1

#radioT = radio.get(index=1)
#radioT2 = radio.get(index=2)

while True:
    led.value = not led.value
    led1.value = not led1.value
    time.sleep(sleepVal)

    # print(bmp280.read_temperature())
    try:
        temp, pressure = bmp280.read_data(bmp280_sensor)
        #print((temp, pressure/50))

    except:
        pass

    #x, y, z = accelermator.get_data(accel)
    #print((x, y, z, ))
    print(f"Temperature {temp} Pressure {pressure}")
    print((temp, ))
    #radio.send(radioT, "Hello from radio")
    #radioBA = radio.read(radioT2)
    #print(radioBA)
    #radioBA = radio.read(radioT)
    radioBA = None
    if radioBA is not None and False:
        radioMsg = radioBA.decode("ascii")
        print(f"Radio Message: {radioMSG}")

