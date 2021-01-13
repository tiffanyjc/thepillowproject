import scipy
from sklearn.neural_network import MLPClassifier
import numpy as np
np.set_printoptions(threshold=np.nan)
import random
import csv



# read from csv, build into np array
training = []
ground_training = []
test = []
ground_test = []
files = ["../jiaju_ma_new_model.csv"]
# files = ["data2_elizabeth_kmeans.csv", "data2_gillians_kmeans.csv"]

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

            if alt:
                training.append(obs_nums)
                ground_training.append((obs[-1]))
                # ground_training.append(int(obs[-1]))
            else:
                test.append(obs_nums)
                ground_test.append((obs[-1]))
                # ground_test.append(int(obs[-1]))

            alt = not alt


# transform dataset first #########################

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Don't cheat - fit only on training data
scaler.fit(training)
training = scaler.transform(training)

# apply same transformation to test data
test = scaler.transform(test)

clf = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
       beta_1=0.9, beta_2=0.999, early_stopping=False,
       epsilon=1e-08, hidden_layer_sizes=(5, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
       solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
       warm_start=False)
clf.fit(training, ground_training)

results = clf.predict(test)

from sklearn.metrics import f1_score
print("f1: " , f1_score(results, ground_test, average='macro'))

correct = 0

for i in range(len(results)):
    
   if results[i] == ground_test[i]:
        results[i] = results[i] == ground_test[i]
        correct += 1

print(correct * 100 / len(results))

