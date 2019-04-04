from pyBusPirateLite.I2Chigh import I2Chigh


class BusPirate:
    def __init__(self):
        i2c = I2Chigh()
        i2c.speed = '400kHz'
        i2c.configure(power=True)

    def read_byte_data(self, i2c_addr, register):
        i2c.get_byte(self, i2c_addr, register)

    def write_byte_data(self, i2c_addr, register, value):
        i2c.set_byte(self, i2c_addr, register, value)
