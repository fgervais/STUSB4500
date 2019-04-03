from pyBusPirateLite.I2C import *


class BusPirate:
    def __init__(self):
        i2c = I2C()
        i2c.speed = '400kHz'
        i2c.configure(power=True)
        i2c.start()
        i2c.transfer([0xec, 0xd0])
        r = i2c.write_then_read(1, 1, [0xed])
        print(f'BME280 ID={hex(r[0])}')

    def read(self, address):
        pass

    def write(self, address):
        pass
