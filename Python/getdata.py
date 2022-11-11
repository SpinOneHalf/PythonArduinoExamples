import serial
import time


def parse_data(data):
    """Cleans up the byte string into and integer"""
    return int(str(data)[2:].split("\\")[0])


# Open port
arduino = serial.Serial(port="/dev/ttyACM0")
# Sleep to let the arduino start
time.sleep(1)
start = time.time()

while True:
    # Read a line of data from arduino
    new_data = parse_data(arduino.readline())
    now = time.time() - start

    print(f"time:{now},data:{new_data}")
