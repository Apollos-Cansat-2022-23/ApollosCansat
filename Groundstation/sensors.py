import adafruit_rfm9x
import board
import digitalio

import deviceCommunication


class Radio:
    def __init__(self, radioType: int):
        locationsCsReset = {
            1: [board.GP6, board.GP7],
            2: [board.GP8, board.GP9]
        }

        csLocation, resetLocation = locationsCsReset[radioType]
        cs = digitalio.DigitalInOut(csLocation)
        reset = digitalio.DigitalInOut(resetLocation)

        successful = False
        i = 0

        while not successful:
            try:
                self.rfm9x = adafruit_rfm9x.RFM9x(deviceCommunication.GetSPI(), cs, reset, 433.0)
                successful = True
            except RuntimeError:
                i += 1
                if i % 100 == 0:
                    print(f"'rfm9x-{radioType}' not detected")

        print(f"RFM9x {radioType} radio ready")

    def read(self, timeout=1):
        return self.rfm9x.receive(timeout=timeout)

    def send(self, message):
        self.rfm9x.send(message)

