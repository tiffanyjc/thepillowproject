import numpy as np
np.set_printoptions(threshold=np.nan)
import csv
import random


def trainer():

    # read from csv, build into np array
    training = []
    ground_training = []
    test = []
    ground_test = []
    # need to figure out a way to clean the data a little
    files = ["jiaju_ma_filtered.csv"]

    for f in files:

        file = open(f, "rt", encoding="utf8")
        reader = csv.reader(file)
        headers = next(reader)

        # for each data point in the csv file, combine into its own vector

        alt = True

        i = 0
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
    scaler = StandardScaler()

    # Don't cheat - fit only on training data
    scaler.fit(training)
    training = scaler.transform(training)

    # apply same transformation to test data
    test = scaler.transform(test)


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

trainer()
