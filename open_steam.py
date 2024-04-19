#!/usr/bin/env python3

import os
from playsound import playsound

def open_steam():
     # play soundeffect
    playsound('sfx/triangle.wav')

    #Open Firefox using the default system command
    os.system("steam")

if __name__ == "__main__":
    open_steam()

