import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c, address=0x48)
chan = AnalogIn(ads, ADS.P0)

print("ADS1015 Analog Input: %0.1f" % chan.value)
