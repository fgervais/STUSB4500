class STUSB4500:
    def __init__(self, i2c_interface, address):
        self.i2c_interface = i2c_interface
        self.address = address
