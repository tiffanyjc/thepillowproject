import serial
import csv

ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=None)


writer = csv.writer(open("data2.csv", "w", encoding="utf8"))


headers = ["time", "accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ", "eulerX", "eulerY", "eulerZ","mic"]

writer.writerow(headers)

while True:


    try:
        # toRead = ser.inWaiting()
        # obs = ser.read().decode("utf-8")
        #
        # print(obs)


        # will accept lines in the format
        obs = ser.readline().decode("utf-8")
        obs = obs.split()
        obs = list(map(float, obs))

        print(obs)

        writer.writerow(obs)
        obs = ser.readline()
    except KeyboardInterrupt:
        break


ser.close()

