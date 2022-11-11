
import serial
import time

def parse_data(data):
    return int(str(data)[2:].split("\\")[0])

arduino=serial.Serial(port="/dev/ttyACM0")
time.sleep(1)
data=[]
times=[]
start=time.time()
while True:
    new_data=parse_data(arduino.readline())
    now=time.time()-start
    data.append(new_data)
    times.append(now)


    print(f"time:{now},data:{new_data}")
