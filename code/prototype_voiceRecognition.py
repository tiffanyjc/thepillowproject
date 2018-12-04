import os
import csv
import time
import signal
import subprocess
from multiprocessing import Process
from playSound import playSound
import googleVUI
import prototype_model_data_collector as prototype
import sdc.py as sleep_collector

myprocess = None

# continuously listens for commands
while True:

    # Passive listening state // only listens for "hey pillow"
    said = (googleVUI.main()).lower()
    print("You said: " + said)

    # Active listening state // listens to all sorts of commands
    if (said == "hey pillow"):
        os.system("espeak -ven+f3 -k5 -s150 'How can I help you?'")
        print("how can I help you? ")

        said = (googleVUI.main()).lower()
        print("You said: " + said)

        # possible commands
        if (said == "recalibrate"):
            print("Okay. Recalibrating.")
            os.system("espeak -ven+f3 -k5 -s150 'Okay. Recalibrating.'")
            prototype.collect(test.csv);
        elif(said == "sleeping"):
            print("Okay. Collecting sleep data.")
            os.system("espeak -ven+f3 -k5 -s150 'Okay. Good night! I will collecting your sleep data.'")
            global myprocess
            myprocess = subprocess.Popen(["python3", "./sdc.py", "overnighttest.csv"])
        elif(said == "stop"):
            print("Okay. Sleep data collection stopped.")
            os.system("espeak -ven+f3 -k5 -s150 'Okay. Good morning.'")
            global myprocess
            global myprocess
            if myprocess != None:
                myprocess.send_signal(signal.SIGINT)
                print("process terminated" + str(myprocess.pid))
            else:
                print("process is null")
        elif (said == "play white noise") or (said == "play rain sounds"):
            print("Okay. Playing rain sounds.")
            playSound("../sounds/rain.mp3")
        else:
            print("Sorry, I did not understand.")
            os.system("espeak -ven+f3 -k5 -s150 'Sorry, I did not understand.'")
