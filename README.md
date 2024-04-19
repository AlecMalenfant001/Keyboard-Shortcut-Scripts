# Keyboard Shortcut Scripts

I have 4 custom hotkeys on my keyboard
<p>&#10065; : Firefox</p> 
<p>&#10061; : Spotify</p>
<p>&#11014; : Steam</p>
<p>&#10005; : Terminal</p>

When I press one of these keys, there is no indicator that the operating system has heard my keyboard event. I would like to add some sort of sound effect that plays before launching the app. Luck for me, Linux Mint makes this super easy for me. 


Under the Shortcuts tab in the Keyboard app there is a button to add your own custom shortcuts where I have commands to launch and kill every app listed above. Except terminal. The shortcut still works; but as of this moment, I cannot explain to you WHY the shortcut still works. Moving on!


Right now the keys are set to open a python file that launches the desired application. 

[Screenshots](https://drive.google.com/drive/folders/1jIc5Jjcmx_rYxuEUJRGeThs9OlnEVY9y?usp=sharing)

Thank you to [Geeks for Geeks](https://www.geeksforgeeks.org/play-sound-in-python/) for teaching me how to play sound files in python. I am going to be using the playsound module.


After adding the playsound function call, this is what the python file that opens Firefox looks like : 

``` Python
import os

from playsound import playsound

  

def open_firefox():

# play soundeffect

playsound('/home/alec/Scripts/sfx/square.wav')

  

"""Opens Firefox using the default system command."""

os.system("firefox")

  

if __name__ == "__main__":

open_firefox()
```


 After adding the the playsound function call to all of the other scripts, I now have a custom sound effect for 3 of my 4 keyboard hotkeys! Fantastic! 




