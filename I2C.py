# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADXL345
# This code is designed to work with the ADXL345_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Accelorometer?sku=ADXL345_I2CS#tabs-0-product_tabset-2

import smbus
import time

def i2cRTX():
    global xAccl
    global yAccl
    global zAccl

    bus = smbus.SMBus(1)

    bus.write_byte_data(0x53, 0x2C, 0x0A)
    bus.write_byte_data(0x53, 0x2D, 0x08)
    bus.write_byte_data(0x53, 0x31, 0x08)

    time.sleep(0.5)

    data0 = bus.read_byte_data(0x53, 0x32)
    data1 = bus.read_byte_data(0x53, 0x33)

    xAccl = ((data1 & 0x03) * 256) + data0
    if xAccl > 511 :
        xAccl -= 1024

    data0 = bus.read_byte_data(0x53, 0x34)
    data1 = bus.read_byte_data(0x53, 0x35)

    yAccl = ((data1 & 0x03) * 256) + data0
    if yAccl > 511 :
        yAccl -= 1024

    data0 = bus.read_byte_data(0x53, 0x36)
    data1 = bus.read_byte_data(0x53, 0x37)

    zAccl = ((data1 & 0x03) * 256) + data0
    if zAccl > 511 :
        zAccl -= 1024

    print ("Acceleration in X,Y,Z-Axis : %d" %xAccl + ', %d' %yAccl + ', %d' %zAccl)
    #time.sleep(1)
    #return xAccl, yAccl, zAccl  
