import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

tecla_del_sistema=  KeyCode(char='t')
clicking=False
controlador_raton= Controller()

def click_isquierdo():
    while True:
        if clicking:
            controlador_raton.click(Button.left,1)
        time.sleep(0.001)

def evento_al_pulsar(llave):
    if llave== tecla_del_sistema:
        global clicking
        clicking=not clicking

monitor_de_tareas=threading.Thread(target=click_isquierdo)
monitor_de_tareas.start()

with Listener(on_press=evento_al_pulsar) as listener:
    listener.join()