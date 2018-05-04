import numpy as np
np.set_printoptions(threshold=np.nan)
import csv
import random


# read from csv, build into np array
training = []
ground_training = []
test = []
ground_test = []
files = ["../prototype_data_tiffany_training.csv"]
# files = ["data2_elizabeth_kmeans.csv", "data2_gillians_kmeans.csv"]

for f in files:

    file = open(f, "rt", encoding="utf8")
    reader = csv.reader(file)
    headers = next(reader)

    # for each data point in the csv file, combine into its own vector

    alt = True

    i = 0
    for obs in reader:

        # add that vector to the greater np array
        obs_nums = list(map(float, obs[1:-1]))

        if random.randint(1, 10) < 8:
            training.append(obs_nums)
            ground_training.append(int(obs[-1]))
        else:
            test.append(obs_nums)
            ground_test.append(int(obs[-1]))

        alt = not alt


# transform dataset first #########################

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Don't cheat - fit only on training data
scaler.fit(training)
training = scaler.transform(training)

# apply same transformation to test data
test = scaler.transform(test)


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

clf.fit(training, ground_training)
print(clf.get_params())
results = clf.score(test, ground_test)
print("mean accuracy: ", results)

results = clf.predict(test)
correct = 0
for i in range(len(results)):
    # results[i] = results[i] == ground_test[i]

    if results[i] == ground_test[i]:
        results[i] = results[i] == ground_test[i]
        correct += 1


print("accuracy: ", correct * 100 / len(results))
