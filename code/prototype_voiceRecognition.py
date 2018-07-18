import os
from playSound import playSound
import googleVUI

# continuously listens for commands
while True:

    # Passive listening state // only listens for "hey pillow"
    said = (googleVUI.main()).lower()
    print("You said: " + said)

    # Active listening state // listens to all sorts of commands
    if (said == "hey pillow"):
        os.system("espeak 'How can I help you?'")
        print("how can I help you? ")

        said = (googleVUI.main()).lower()
        print("You said: " + said)

        # possible commands
        if (said == "recalibrate"):
            print("Okay. Recalibrating.")
            os.system("espeak 'Okay. Recalibrating.'")
            import prototype_model_data_collector as prototype
        elif (said == "play white noise") or (said == "play rain sounds"):
            print("Okay. Playing rain sounds.")
            playSound("../sounds/rain.mp3")
        else:
            print("Sorry, I did not understand.")
            os.system("espeak 'Sorry, I did not understand.'")
