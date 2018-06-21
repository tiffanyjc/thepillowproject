# The Pillow Project

> A Brown HCI Group Research Project
> Prototype developed by Tiffany Chen as her senior thesis

## Dependencies
* Python 3
* Arduino

## Hardware
* Raspberry Pi 3 Model B+
* Arduino Uno
* Adafruit BNO055
* FSR

## Scripts
* prototype_voiceRecognition.py
	* Uses Google Speech Recognition API to listen to initialization commands.
	* Triggers calibration script.

* prototype_model_data_collector.py
	* Calibration Script. Collects data for model training.

* prototype_sleep_data_collector.py
	* Collects data during sleep. Needs to be started manually.

* prototype_classifier_decisiontree.py
	* Trains the model with data collected during calibration. The model is then used to classify data collected during sleep.
	* Can be changed to use other machine learning models.

* prototype_sendData.py
	* Sends data files to SleepCoacher server. 

