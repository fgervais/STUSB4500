from pyBusPirateLite.I2Chigh import I2Chigh

class BusPirate:
    def __init__(self):
        self.i2c = I2Chigh()
        self.i2c.speed = '400kHz'
        self.i2c.configure(power=True, pullup=True)

    def read_byte_data(self, i2c_addr, register):
        return self.i2c.get_byte(i2c_addr, register)

    def write_byte_data(self, i2c_addr, register, value):
        self.i2c.set_byte(i2c_addr, register, value)
