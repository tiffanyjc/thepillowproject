import serial
import csv
import pygame
import prototype_classifier_decisiontree as tree
import os
import time
import class_collector as classes
import sys

# collects data during calibration period and immediately trains decision tree model

def collect(filename):
    # initializing things
    numIters = 8 # number of positions to cycle through during calibration
    iterLength = 20 # number of loops each position should be held for
    ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=None)
    pygame.init()
    file = open(filename, "w", encoding="utf8")
    writer = csv.writer(file)

    positionFlow = classes.collect()

    # set up headers
    headers = ["time", "accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ", "eulerX", "eulerY", "eulerZ", "mic"]

    for i in range(1, 324):
        headers.append("key" + str(i))

    headers.append("ground")
    writer.writerow(headers)

    current = "right"
    print("current: ", current)
    os.system("say 'please turn onto your '")
    os.system(positionFlow[current]["command"])

    start = time.time()
    iter = 1
    while iter <= numIters:
        # for iter in range (0, numIters):
        try:
            # read data from arduino
            obs = ser.readline().decode("utf-8")
            obs = obs.split()
            obs = list(map(float, obs))
            # print(obs[0])
            # epoch time
            obs[0] = float(time.time())

            # read from keyboard, append each as binary to obs
            pygame.event.get()
            keypressed = pygame.key.get_pressed()

            for k in keypressed:
                obs.append(k)

            # append ground truth
            obs.append(positionFlow[current]["ground"])

            writer.writerow(obs)
            obs = ser.readline()

            # change positions
            if (time.time() - start > iterLength) and iter == numIters:
                break
            elif (time.time() - start > iterLength):
                current = positionFlow[current]["next"]
                print("current: ", current)
                os.system("say 'please turn onto your '")
                os.system(positionFlow[current]["command"])
                time.sleep(2)
                print("continue")
                start = time.time()
                iter += 1

        except KeyboardInterrupt:
            break

    file.close()
    os.system("say 'this study is done. thank you.'")
    ser.close()

    print("training decision tree model")
    tree.trainer(filename, '')


# when it's executed on command line
if __name__ == "__main__":
    first_arg = sys.argv[1]
    collect(first_arg)