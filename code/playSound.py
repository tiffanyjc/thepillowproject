import pygame
import time

# spins up a temporary pygame class to play an audio file
def playSound(filename):
    pygame.init()
    pygame.mixer.init()  # Initialize the mixer module.
    pygame.mixer.music.load(filename)  # Load a sound.
    pygame.mixer.music.play()
    time.sleep(1)


# for testing
playSound('../sounds/confirmationBeep.wav')