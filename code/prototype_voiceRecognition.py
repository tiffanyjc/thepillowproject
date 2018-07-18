# import speech_recognition as sr
import speech_recognition as sr
import os
from playSound import playSound
# import google-api-python-client

# obtain audio from the microphone
r = sr.Recognizer()
print("Say something!")

# continuously listens for commands
while True:

    with sr.Microphone() as source:
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        said = r.recognize_google(audio).lower()
        print("You said: " + said)

        # only activate when user says "hey pillow"
        if (said == "hey pillow"):
            os.system("espeak 'How can I help you?'")
            print("how can I help you? ")

            with sr.Microphone() as source:
                audio = r.listen(source)

            try:
                said = r.recognize_google(audio).lower()
                print("You said: " + said)

                # possible commands
                if (said == "recalibrate"):
                    os.system("espeak 'Okay. Recalibrating.'")
                    import prototype_model_data_collector as prototype
                elif (said == "play white noise") or (said == "play rain sounds"):
                    playSound("../sounds/rain.mp3")
                else:
                    os.system("espeak 'Sorry, I did not understand.'")

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                os.system("espeak 'Sorry, I did not understand.'")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                os.system("espeak 'Sorry, I can't take your request at this time'")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
