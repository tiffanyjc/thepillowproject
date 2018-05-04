import speech_recognition as sr
import os

# obtain audio from the microphone
r = sr.Recognizer()
print("Say something!")

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
        if (said == "hey google"):
            os.system("say 'How can I help you?'")

            with sr.Microphone() as source:
                audio = r.listen(source)

            try:
                said = r.recognize_google(audio).lower()
                print("You said: " + said)

                if (said == "recalibrate"):
                    os.system("say 'Okay. Recalibrating.'")
                    import prototype_model_data_collector as prototype

                else:
                    os.system("say 'Sorry, I did not understand.'")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                os.system("say 'Sorry, I did not understand.'")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                os.system("say 'Sorry, I can't take your request at this time'")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
