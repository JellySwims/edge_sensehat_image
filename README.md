# CHI@Edge Waveshare sense pi-hat image
Trovi Artifact outlining how to enable the usage of the waveshare sense hat through both the i2c and gpio interface 

## Required device boot options and device tree overlays
- dtparam=i2c_arm=on is used to enable the i2c interface on the raspberry pi
- dtoverlay=gpio is used to enable the gpio interface on the raspberry pi

## Required /dev devices to be included in the device profile
- /dev/i2c-0
- /dev/i2c-1
- /dev/gpiomem
- /dev/gpiochip0
- /dev/gpiochip1

## Required dependencies to drive the sensors
- python3
- i2c-tools
- adafruit-blinka 
- rpilgpio
- more (see Dockerfile)
