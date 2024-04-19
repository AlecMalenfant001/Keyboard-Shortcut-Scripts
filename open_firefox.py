#!/usr/bin/env python3

import os
from playsound import playsound

def open_firefox():
    # play soundeffect
    playsound('sfx/square.wav')

    #Opens Firefox using the default system command.
    os.system("firefox")

if __name__ == "__main__":
    open_firefox()

