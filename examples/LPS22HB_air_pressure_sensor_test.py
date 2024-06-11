import board
import busio
import adafruit_lps2x

i2c = busio.I2C(board.SCL, board.SDA)
lps = adafruit_lps2x.LPS22(i2c, address=0x5C)

print("LPS22HB Pressure: %0.1f hPa" % lps.pressure)
print("LPS22HB Temperature: %0.1f C" % lps.temperature)
