import numpy as np
np.set_printoptions(threshold=np.nan)
import csv
import random
import sys
import datetime


def trainer(trainingData, rawData):

    # read from csv, build into np array
    training = []
    ground_training = []
    test = []
    ground_test = []
    # need to figure out a way to clean the data a little
    # files = ["jiaju_ma_filtered.csv"]

    # for f in files:

    file = open(trainingData, "rt", encoding="utf8")
    reader = csv.reader(file)
    headers = next(reader)

    # for each data point in the csv file, combine into its own vector
    # alt = True
    #
    # i = 0

    for obs in reader:
        if len(obs) == len(headers):

            # add that vector to the greater np array
            obs_nums = list(map(float, obs[1:-1]))

            if random.randint(1, 10) < 6:
                training.append(obs_nums)
                ground_training.append(obs[-1])
            else:
                test.append(obs_nums)
                ground_test.append(obs[-1])


    # transform dataset first #########################

    from sklearn.preprocessing import StandardScaler
    # scaler = StandardScaler()

    # Don't cheat - fit only on training data
    # scaler.fit(training)
    # training = scaler.transform(training)

    # apply same transformation to test data
    # test = scaler.transform(test)


    from sklearn import svm
    clf = svm.SVC()


    clf.fit(training, ground_training)

    results = clf.predict(test)
    print(results)


    from sklearn.metrics import f1_score
    print("f1: " , f1_score(results, ground_test, average='weighted'))

    correct = 0

    for i in range(len(results)):
        # results[i] = results[i] == ground_test[i]

        if results[i] == ground_test[i]:
            #results[i] = results[i] == ground_test[i]
            correct += 1


    print("accuracy: ", correct * 100 / len(results))

    #######################################
    ##### USE MODEL FOR PREDICTING #######
    #######################################

    # for predicting behaviors
    if rawData != '':
        try:
            data = []
            times = []
            file = open(rawData, "rt", encoding="utf8")
            reader = csv.reader(file)
            headers = next(reader)

            for obs in reader:
                # gets rid of some missed data at beginning
                if len(obs) == len(headers):
                    obs_nums = list(map(float, obs[0:-1]))
                    data.append(obs_nums[1:])
                    times.append(obs_nums[0])

            results = clf.predict(data)
            print(results)

            # get position and duration
            rprev = ''
            rprev = results[0]
            tstart = times[0]

            totalTime = 0

            for i in range(1, len(results)):

                # condition for changing positions
                if results[i] != rprev or i == (len(results) - 1):

                    # cut out noise
                    if times[i] - tstart >= 1:
                        print(
                            datetime.datetime.fromtimestamp(tstart).strftime('%Y-%m-%d %H:%M:%S'),
                            ": ",
                            rprev, " for ",
                            round(times[i] - tstart, 2), " secs")

                        totalTime += times[i] - tstart
                        tstart = times[i]
                        rprev = results[i]

            print("\nsleep time (secs): ", totalTime)


        except OSError as e:
            print('Invalid filename for raw data. Try again.')

# when it's executed on command line
if __name__ == "__main__":
    first_arg = sys.argv[1]

    if len(sys.argv) == 1:
        print("need to provide a filename with training data")
    elif len(sys.argv) == 2:
        second_arg = ''
    else:
        second_arg = sys.argv[2]
    trainer(first_arg, second_arg)

# original
# trainer()
