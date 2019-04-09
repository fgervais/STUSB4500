class Cable:
    MASK_ATTACHED_STATUS = 0x01
    VALUE_ATTACHED = 1

    MASK_REVERSE = 0x80
    CC1_ATTACHED = 0
    CC2_ATTACHED = 1


    def __init__(self, stusb4500):
        self.stusb4500 = stusb4500

    def __str__(self):
        if self.attached:
            string = "Cable attached "
            if not self.reversed:
                string += "[CC1]"
            else:
                string += "[CC2]"
        else:
            string = "Cable not attached"

        return string

    @property
    def attached(self):
        port_status = self.stusb4500[STUSB4500.Register.PORT_STATUS]
        return ((port_status & Cable.MASK_ATTACHED_STATUS)
                    == Cable.VALUE_ATTACHED)

    @property
    def reversed(self):
        typec_status = self.stusb4500[STUSB4500.Register.TYPE_C_STATUS]
        return (typec_status & Cable.MASK_REVERSE) == Cable.CC2_ATTACHED


class STUSB4500:

    class Register:
        PORT_STATUS = 0x0E
        TYPE_C_STATUS = 0x15
        DEVICE_ID = 0x2F

        LAST = 0x94


    def __init__(self, i2c_interface, i2c_address):
        self.i2c_interface = i2c_interface
        self.i2c_address = i2c_address

        self.cable = Cable(self)

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
