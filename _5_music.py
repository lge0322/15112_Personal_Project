import pygame

from pygame.locals import *

from _1_classes import *

pygame.mixer.init()

#music cited: https://downloads.khinsider.com/game-soundtracks/album/nintendo-switch-sound-effects

def backgroundMusic():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("backgroundMusic.mp3"))

#music cited: https://downloads.khinsider.com/game-soundtracks/album/nintendo-switch-sound-effects

def gemMusic():
    pygame.mixer.music.load("Gem.mp3")
    pygame.mixer.music.play()

#music cited: https://downloads.khinsider.com/game-soundtracks/album/nintendo-switch-sound-effects

def buttonMusic():
    pygame.mixer.music.load("Button.mp3")
    pygame.mixer.music.play(1)

#music cited: https://downloads.khinsider.com/game-soundtracks/album/fireboy-and-watergirl

def switchMusic():
    pygame.mixer.music.load("S.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(20)

#music cited: https://downloads.khinsider.com/game-soundtracks/album/fireboy-and-watergirl

def doorOpenMusic():
    pygame.mixer.music.load("Dooropen.mp3")
    pygame.mixer.music.play()

#music cited: https://downloads.khinsider.com/game-soundtracks/album/fireboy-and-watergirl

def dieMusic():
    pygame.mixer.music.load("Die.mp3")
    pygame.mixer.music.play()





