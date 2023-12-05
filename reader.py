import serial
import sys
import csv
import time

# [Timestamp, Right, Left]

ser = serial.Serial(
    port=sys.argv[1],
    baudrate=115200,
    timeout=0)

print("connected to: " + ser.portstr)
start = round(time.time() * 1000)

with open(str(time.time()) + '.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerow(['time', 'reading'])
    last = round(time.time() * 1000)

    old_r0 = -1

    while True:
        try:
            mills = round(time.time() * 1000)
            last = mills

            val = ser.readline()
            while '\\n' not in str(val):
                temp = ser.readline()
                if not not temp.decode():
                    val = (val.decode() + temp.decode()).encode()
            val = val.decode()[:-2]
            res = val.split(';')

            if int(float(res[0])) != old_r0:
                old_r0 = int(float(res[0]))
                towrite = [start + int(float(res[0])), float(res[1]) if float(res[1]) >= 0 else 0]
                print(towrite)
                writer.writerow(towrite)
        except UnicodeDecodeError as e:
            pass

