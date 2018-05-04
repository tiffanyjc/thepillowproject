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


from sklearn import linear_model
clf = linear_model.LinearRegression()

clf.fit(training, ground_training)
# print(clf.coef_)
results = clf.score(test, ground_test)

print("mean accuracy: ", results)
results = clf.predict(test)

from sklearn.metrics import mean_squared_error
print("MSE: ", mean_squared_error(ground_test, results))

from sklearn.metrics import r2_score
print(r2_score(ground_test, results))
