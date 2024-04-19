#!/bin/bash
import os
from playsound import playsound

def kill_spotify():
    # play soundeffect
    playsound('sfx/kill.wav')

    #kill program
    os.system("pkill spotify")

if __name__ == "__main__":
    kill_spotify()