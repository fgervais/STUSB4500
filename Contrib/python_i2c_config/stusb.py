class STUSB4500:

    class Register:
        DEVICE_ID = 0x2F

        LAST = 0x94


    def __init__(self, i2c_interface, i2c_address):
        self.i2c_interface = i2c_interface
        self.i2c_address = i2c_address

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self.i2c_interface.read_byte_data(self.i2c_address, i)
                for i in range(*key.indices(STUSB4500.Register.LAST))]
        else:
            return self.i2c_interface.read_byte_data(self.i2c_address, key)

    def __setitem__(self, key, value):
        if key > STUSB4500.Register.LAST:
            raise IndexError("list index out of range")

        self.i2c_interface.write_byte_data(self.i2c_address, key, value)

    @property
    def device_id(self):
        self[STUSB4500.Register.DEVICE_ID]
