import board
import busio
from adafruit_bus_device.i2c_device import I2CDevice

DEVICE_ADDRESS = 0x46

class SenseHATLEDs:
    def __init__(self, i2c_bus, address=DEVICE_ADDRESS):
        self.i2c_device = I2CDevice(i2c, address)
        self.clear()

    def clear(self):
        self.pixels = [0] * (8 * 8 * 3 + 1)

    def set_pixel(self, x, y, red, green, blue):
        linear_addr = x * 8 + y
        r_addr = (y * 24) + x + 1
        g_addr = r_addr + 8
        b_addr = g_addr + 8
        self.pixels[r_addr] = int(red * 63)
        self.pixels[g_addr] = int(green * 63)
        self.pixels[b_addr] = int(blue * 63)

    def update(self):
        with self.i2c_device as display:
            display.write(bytearray(self.pixels))

i2c = board.I2C()
display = SenseHATLEDs(i2c)
display.clear()
display.update()
print("display cleared")
