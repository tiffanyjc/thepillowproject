import csv

# collects the order of classes to be used during the calibration period
def collect():
    # initializing things
    file = open("classes.csv", "rt", encoding="utf8")
    reader = csv.reader(file)
    headers = next(reader)
    positionFlow = {}

    # csv header order: class // ground // next class // spoken command

    for obs in reader:

        # eg. right
        obsClass = obs[0]
        positionFlow[obsClass] = {}

        for i in range(len(headers)):
            if i:
                positionFlow[obsClass][headers[i]] = obs[i]

        positionFlow[obsClass]['command'] = "say '" + positionFlow[obsClass]['command'] + "'"

    file.close()

    return positionFlow

# collect()