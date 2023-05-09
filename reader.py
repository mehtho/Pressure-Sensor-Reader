import serial
import sys
import csv
import time

ser = serial.Serial(
    port=sys.argv[1],
    baudrate=9600,
    timeout=0)

print("connected to: " + ser.portstr)

with open(str(time.time()) + '.csv', 'w') as f:
    count = 0
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerow(['time', 'reading'])

    while True:
        line = ser.readline()
        if line:
            towrite = [str(count), line.decode('utf-8')[:-2]]
            writer.writerow(towrite)
            print(towrite)
            count += 1


