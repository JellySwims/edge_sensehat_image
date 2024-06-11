import board
import busio
import adafruit_tcs34725

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c, address=0x29)

print("TCS34725 Color: ", sensor.color_rgb_bytes)
