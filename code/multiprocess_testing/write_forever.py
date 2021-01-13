import csv
import time
import sys
import signal
import os

def sig_handler (signum, frame):
    #print debugging information
    #print ('got', signum, 'signal, closing file...')
    #close the file before exiting
    #file.close()
    #print ('exiting')
    #exit. you have to write this to end the program from here
    sys.exit(1)
    return

def writeToCSV():
    signal.signal (signal.SIGINT, sig_handler)
    file = open("forever.csv", "w", encoding="utf8")
    writer = csv.writer(file)
    #print("writing begins")
    while True:
        writer.writerow("haha");
        time.sleep(1);

if __name__ == '__main__':
    writeToCSV();
