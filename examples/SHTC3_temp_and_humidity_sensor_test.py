import board
import busio
import adafruit_shtc3

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_shtc3.SHTC3(i2c)

print("SHTC3 Temperature: %0.1f C" % sensor.temperature)
print("SHTC3 Humidity: %0.1f %%" % sensor.relative_humidity)
