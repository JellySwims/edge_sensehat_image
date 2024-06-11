# Use the balenalib image for Raspberry Pi as the base image
FROM balenalib/raspberrypi3-64-debian:bookworm

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV UDEV=1

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-smbus \
    i2c-tools \
    libgpiod2 \
    gpiod \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install Adafruit Blinka and rpi-lgpio within the virtual environment
RUN pip install --upgrade setuptools \
    && pip install adafruit-blinka adafruit-circuitpython-ads1x15 adafruit-circuitpython-icm20x adafruit-circuitpython-lps2x adafruit-circuitpython-shtc3 adafruit-circuitpython-tcs34725 rpi-lgpio

# Copy Adafruit example scripts to /examples
COPY examples /examples

CMD ["sleep", "infinity"]
