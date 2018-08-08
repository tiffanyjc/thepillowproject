import numpy as np
np.set_printoptions(threshold=np.nan)
import csv
import random
import sys
import datetime
import prototype_confusionmatrix as cm_maker

from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion="entropy")
# clf = tree.DecisionTreeClassifier()

# to create confusion matrix
def print_cm(cm, labels, hide_zeroes=False, hide_diagonal=False, hide_threshold=None):
    """pretty print for confusion matrixes"""
    columnwidth = max([len(x) for x in labels] + [5])  # 5 is value length
    empty_cell = " " * columnwidth
    # Print header
    print("    " + empty_cell, " ")
    for label in labels:
        print("%{0}s".format(columnwidth) % label, " ")
    print()
    # Print rows
    for i, label1 in enumerate(labels):
        print("    %{0}s".format(columnwidth) % label1, " ")
        for j in range(len(labels)):
            cell = "%{0}.1f".format(columnwidth) % cm[i, j]
            if hide_zeroes:
                cell = cell if float(cm[i, j]) != 0 else empty_cell
            if hide_diagonal:
                cell = cell if i != j else empty_cell
            if hide_threshold:
                cell = cell if cm[i, j] > hide_threshold else empty_cell
            print(cell, " ")
        print()

# trainingData is the csv with calibration data
# rawData is a list of files with sleepData
def trainer(trainingData, rawData):

    # read from csv, build into np array
    training = []
    ground_training = []
    test = []
    ground_test = []
    random.seed(3)

    file = open(trainingData, "rt", encoding="utf8")
    reader = csv.reader(file)
    headers = next(reader)

    #########################################
    ##### DATA CLEANING / PREP IN CSV #######
    #########################################

    for obs in reader:
        # gets rid of some missed data at beginning

        if len(obs) == len(headers):

            # add that vector to the greater np array
            obs_nums = list(map(float, obs[1:-1]))

            if random.randint(1, 10) < 7:
                training.append(obs_nums)
                ground_training.append(obs[-1])
            else:
                test.append(obs_nums)
                ground_test.append(obs[-1])

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()

    # Don't cheat - fit only on training data
    # scaler.fit(training)
    # training = scaler.transform(training)

    # apply same transformation to test data
    # test = scaler.transform(test)

    #######################################
    ##### TRAIN AND VALIDATE MODEL #######
    #######################################

    # from sklearn import tree
    # clf = tree.DecisionTreeClassifier()

    clf.fit(training, ground_training)
    # tree.export_graphviz(clf, out_file="tree.dot")

    results = clf.score(test, ground_test)
    print("\nmodel accuracy: ", results)
    print("\n")

    results = clf.predict(test)
    print(results)

    from sklearn.metrics import confusion_matrix

    labels = ["right", "stomach", "left", "back"]

    cm = confusion_matrix(ground_test, results)
    print("confusion matrix: \n")
    print_cm(cm, labels)
    print("\n")


    # cm_maker.print_conf_matrix(ground_test, results, labels)

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
                # gets rid of some missed data at beginning [0:-1]
                if len(obs) == len(headers):
                    obs_nums = list(map(float, obs[0:-1]))
                    data.append(obs_nums[1:])
                    times.append(obs_nums[0])

            # data = scaler.transform(test)
            results = clf.predict(data)
            # tree.export_graphviz(clf, out_file="tree_2.dot")
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
