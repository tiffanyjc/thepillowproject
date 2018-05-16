import requests
import csv
import sys

# sends data collected from user with ID from filename to Sleepcoacher server
def sendData(filename, ID):
    # api endpoint
    API_ENDPOINT = "http://sleep.cs.brown.edu:443"

    # first clean data of any faulty / incomplete data
    fileR = open(filename, "rt", encoding="utf8")
    fileW = open("temp.csv", "w", encoding="utf8")
    reader = csv.reader(fileR)
    writer = csv.writer(fileW)

    headers = next(reader)
    writer.writerow(headers)

    for obs in reader:
        if len(obs) == len(headers):
            writer.writerow(obs)

    fileR.close()
    fileW.close()

    file = open("temp.csv", "rt", encoding="utf8")

    # send cleaned data to server
    data = file.read()
    data += "&PillowistUser="
    data += ID

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data)

# execution: python prototype_sendData.py [filename] ID
if __name__ == "__main__":
    first_arg = sys.argv[1]
    second_arg = sys.argv[2]
    sendData(first_arg, second_arg)
    print("data sent!")