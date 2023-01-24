import adafruit_lis3dh

def setup(i2c):
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)
    #lis3dh.range = adafruit_lis3dh.RANGE_2_G

    return lis3dh

def get_data(lis3dh):
    #return [val for val in lis3dh.orientation]
    #return [val for val in lis3dh.acceleration]
    return [
        value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration
    ]
