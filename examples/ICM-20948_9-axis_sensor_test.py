import board
import busio
import adafruit_icm20x

i2c = busio.I2C(board.SCL, board.SDA)
icm = adafruit_icm20x.ICM20948(i2c, address=0x68)

print("ICM-20948 Acceleration: ", icm.acceleration)
print("ICM-20948 Gyro: ", icm.gyro)
print("ICM-20948 Magnetometer: ", icm.magnetic)
