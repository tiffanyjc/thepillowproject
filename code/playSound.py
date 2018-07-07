import pygame
import time

# spins up a temporary pygame class to play a sound
def playSound(filename):
    pygame.init()
    pygame.mixer.init()  # Initialize the mixer module.
    sound1 = pygame.mixer.Sound(filename)  # Load a sound.
    sound1.play()
    time.sleep(1)

# for testing
# playSound('../sounds/ding.wav')