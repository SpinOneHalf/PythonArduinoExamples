import serial
import time
arduino=serial.Serial(port="/dev/ttyACM0")
time.sleep(1)
results=arduino.readline()
print(results)