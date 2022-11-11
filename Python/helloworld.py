import serial
import time

# Very simple example of how to use py serial with arduino
# Note: The port may be different on different computers!! check if arduino IDE
arduino = serial.Serial(port="/dev/ttyACM0",baudrate=9600)
time.sleep(1)
results = arduino.readline()
print(results)
