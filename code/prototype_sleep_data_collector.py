import serial
import csv
import pygame
import time
import prototype_sendData as sender
import sys

# collects and writes sleeping data to the giving csv filename
def collect(filename):
    # initializing things -- serial port URL should be from whichever USB port the arduino is connected to
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=None)
    pygame.init()
    file = open(filename, "w", encoding="utf8")
    writer = csv.writer(file)

    # change this if you want to use a different userID
    userID = "1234"

    # set up headers
    headers = ["time", "accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ", "eulerX", "eulerY", "eulerZ", "mic"]

    for i in range(1, 324):
        headers.append("key" + str(i))

    writer.writerow(headers)

    # continuously collect datapoints
    while True:
        try:
            # read data from arduino
            obs = ser.readline().decode("utf-8")
            obs = obs.split()
            obs = list(map(float, obs))

            # epoch time
            obs[0] = float(time.time())

            # read from keyboard, append each as binary to obs
            pygame.event.get()
            keypressed = pygame.key.get_pressed()

            for k in keypressed:

                obs.append(k)

            writer.writerow(obs)
            obs = ser.readline()

        except KeyboardInterrupt:
            break

    file.close()
    ser.close()

    # send data to SleepCoacher server
    sender.sendData(filename, userID)
    print("data sent!")

# when it's executed on command line
if __name__ == "__main__":
    first_arg = sys.argv[1]
    collect(first_arg)