#!/usr/bin/env python3

import os
from playsound import playsound

def open_spotifyf():
    # play soundeffect
    playsound('/home/alec/Scripts/sfx/circle.wav')

    """Opens Firefox using the default system command."""
    os.system("spotify")

if __name__ == "__main__":
    open_spotifyf()

