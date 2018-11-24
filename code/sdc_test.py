import serial
import csv
import pygame
import time
import prototype_sendData as sender
import sys

# collects and writes sleeping data to the giving csv filename
def collect(filename):
    # initializing things -- serial port URL should be from whichever USB port the arduino is connected to
    ser = serial.Serial('COM4', 9600, timeout=None)
    pygame.init()
    file = open(filename, "w", encoding="utf8")
    writer = csv.writer(file)

    # change this if you want to use a different userID
    #userID = "valerie_nguon@brown.edu"
    userID = "jiaju_ma@brown.edu"

    # set up headers
    headers = ["time", "accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ", "eulerX", "eulerY", "eulerZ", "mic"]

    # changed to FSR pressure grid
    for i in range(20):
        headers.append("FSR" + str(i))

    writer.writerow(headers)

    print("being collecting")
    # continuously collect datapoints
    while True:
        try:
            # read data from arduino
            obs = ser.readline().decode("utf-8")
            obs = obs.split()
            obs = list(map(float, obs))

            if (len(obs) > 10):
                # epoch time
                obs[0] = float(time.time())

                writer.writerow(obs)
                obs = ser.readline()

        except KeyboardInterrupt:
            break

    file.close()
    ser.close()

    # send data to SleepCoacher server
    #sender.sendData(filename, userID)
    #print("data sent!")

# when it's executed on command line
if __name__ == "__main__":
    try:
        first_arg = sys.argv[1]
        collect(first_arg)
    except IndexError:
        print("Missing argument: need to provide filename to write data to.")
