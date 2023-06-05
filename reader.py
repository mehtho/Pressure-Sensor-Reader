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
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerow(['time', 'reading'])
    last = round(time.time() * 1000)
    while True:
        mills = round(time.time() * 1000)
        if mills > last + 9:
            last = mills

            val = ser.readline()
            while '\\n' not in str(val):
                time.sleep(.001)
                temp = ser.readline()
                if not not temp.decode():
                    val = (val.decode() + temp.decode()).encode()
            val = val.decode()[:-2]

            towrite = [mills, val]
            print(towrite)
            writer.writerow(towrite)
