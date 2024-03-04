import serial
import time

# Set up the serial connection to the GPS module
# Replace '/dev/ttyS0' with the correct serial port if necessary
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

def read_gps_data():
    try:
        while True:
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(data)
                # You can parse the data here to extract latitude, longitude, etc.
            time.sleep(1)
    except KeyboardInterrupt:
        print("GPS reading stopped.")
    finally:
        ser.close()

if __name__ == '__main__':
    read_gps_data()

