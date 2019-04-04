class STUSB4500:
    LAST_REGISTER_ADDR = 0x94


    def __init__(self, i2c_interface, i2c_address):
        self.i2c_interface = i2c_interface
        self.i2c_address = i2c_address

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self.i2c_interface.read_byte_data(self.i2c_address, i)
                for i in range(*key.indices(STUSB4500.LAST_REGISTER_ADDR))]
        else:
            return self.i2c_interface.read_byte_data(self.i2c_address, key)

    def __setitem__(self, key, value):
        if key > STUSB4500.LAST_REGISTER_ADDR:
            raise IndexError("list index out of range")

        self.i2c_interface.write_byte_data(self.i2c_address, key, value)
