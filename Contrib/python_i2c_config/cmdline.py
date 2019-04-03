import i2c_interface

from stusb import STUSB4500


interface = i2c_interface.BusPirate()
stusb4500 = STUSB4500(interface, 0x28)
