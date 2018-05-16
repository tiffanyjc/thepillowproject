import serial
import csv
import pygame
import prototype_classifier_decisiontree as tree
import os
import time
import class_collector as classes

# same as prototype_model_data_collector but calibrates for head angle rather than sleeping position

def collect():
    # initializing things
    numIters = 10
    iterLength = 15
    ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=None)
    pygame.init()
    file = open("prototype_data_tiffany_training.csv", "w", encoding="utf8")
    writer = csv.writer(file)

    positionFlow = classes.collect()

    # set up headers
    headers = ["time", "accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ", "eulerX", "eulerY", "eulerZ", "mic"]

    for i in range(1, 324):
        headers.append("key" + str(i))

    headers.append("ground")
    writer.writerow(headers)

    current = "-45"
    print("current: ", current)
    os.system("say 'please turn '")
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
                os.system("say 'please turn'")
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
    tree.trainer()

collect()