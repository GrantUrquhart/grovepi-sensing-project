import time
from grove.i2c import Bus
from smbus2 import SMBus, i2c_msg

SGP41_I2C_ADDR = 0x59  # SGP41 I2C address

# Commands for SGP41
INIT_AIR_QUALITY = [0x20, 0x03]
MEASURE_RAW_SIGNALS = [0x26, 0x0F]

def read_sgp41(bus):
    # Initialize air quality measurement
    bus.write_i2c_block_data(SGP41_I2C_ADDR, INIT_AIR_QUALITY[0], INIT_AIR_QUALITY[1:])

    time.sleep(1)  # Wait for the sensor to initialize

    # Measure raw signals
    bus.write_i2c_block_data(SGP41_I2C_ADDR, MEASURE_RAW_SIGNALS[0], MEASURE_RAW_SIGNALS[1:])
    time.sleep(0.05)  # Short delay before reading data

    # Read 6 bytes of data (2 bytes for each signal)
    data = bus.read_i2c_block_data(SGP41_I2C_ADDR, 0, 6)

    # Convert the data to 16-bit integers
    signal1 = (data[0] << 8) | data[1]
    signal2 = (data[3] << 8) | data[4]

    return signal1, signal2

if __name__ == "__main__":
    bus = SMBus(1)  # Use I2C bus 1

    try:
        while True:
            s1, s2 = read_sgp41(bus)
            print(f"Signal 1: {s1}, Signal 2: {s2}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by user")
    finally:
        bus.close()
