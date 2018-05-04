import csv

def collect():
    # initializing things
    file = open("classes.csv", "rt", encoding="utf8")
    reader = csv.reader(file)
    headers = next(reader)
    positionFlow = {}

    # csv header order: class // ground // next // command

    for obs in reader:

        # eg. right
        obsClass = obs[0]
        positionFlow[obsClass] = {}

        for i in range(len(headers)):
            if i:
                positionFlow[obsClass][headers[i]] = obs[i]

        # positionFlow[obsClass]['ground'] = int(positionFlow[obsClass]['ground'])
        positionFlow[obsClass]['command'] = "say '" + positionFlow[obsClass]['command'] + "'"

    # print(positionFlow["front"])
    file.close()

    return positionFlow

# collect()