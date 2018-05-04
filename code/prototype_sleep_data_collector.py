import serial
import csv
import pygame
import time
import prototype_sendData as sender
import sys

def collect(filename):
    # initializing things
    ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=None)
    pygame.init()
    file = open(filename, "w", encoding="utf8")
    writer = csv.writer(file)
    userID = "1234"

    # set up headers
    headers = ["time", "accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ", "eulerX", "eulerY", "eulerZ", "mic"]

    for i in range(1, 324):
        headers.append("key" + str(i))

    writer.writerow(headers)

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
    sender.sendData(filename, userID)
    print("data sent!")

# when it's executed on command line
if __name__ == "__main__":
    first_arg = sys.argv[1]
    collect(first_arg)