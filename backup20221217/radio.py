# Write your code here :-)
import digitalio
import board
import busio
import adafruit_rfm9x

pins = {
	0: board.GP0,
	1: board.GP1,
	2: board.GP2,
	3: board.GP3,
	4: board.GP4,
	5: board.GP5,
	6: board.GP6,
	7: board.GP7,
	8: board.GP8,
	9: board.GP9,
	10: board.GP10,
	11: board.GP11,
	12: board.GP12,
	13: board.GP13,
	14: board.GP14,
	15: board.GP15,
	16: board.GP16,
	17: board.GP17,
	18: board.GP18,
	19: board.GP19,
	20: board.GP20,
	21: board.GP21,
	22: board.GP22,
	23: board.GP23,
	24: board.GP24,
	25: board.GP25,
	26: board.GP26,
	27: board.GP27,
	28: board.GP28
}


spi = busio.SPI(clock=pins[2], MOSI=pins[3], MISO=pins[4])

cs1 = digitalio.DigitalInOut(board.GP6)
reset1 = digitalio.DigitalInOut(board.GP7)

cs2 = digitalio.DigitalInOut(board.GP8)
reset2 = digitalio.DigitalInOut(board.GP9)

def get(index=1):
    if index == 1:
        rfm9x = adafruit_rfm9x.RFM9x(spi, cs1, reset1, 433.0)
    elif index == 2:
        rfm9x = adafruit_rfm9x.RFM9x(spi, cs2, reset2, 433.0)
    else:
        raise Exception("Invalid Index Count")
    print(f"RFM9x {index} radio ready")

    return rfm9x

def send(radioT, message):
    radioT.send(message)
    print("Radio Message Sent")

def read(radioT):
    return radioT.receive(timeout=1.0)
