import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGLE_KEY=  KeyCode(char='t')
clicking=False
mause= Controller()

def clicker():
    while True:
        if clicking:
            mause.click(Button.left,1)
        time.sleep(0.001)

def toggle_event(key):
    if key== TOGLE_KEY:
        global clicking
        clicking=not clicking

click_thread=threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()