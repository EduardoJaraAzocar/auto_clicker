import time
import threading
import tkinter as tk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
########################################################################
def click_isquierdo():
    while True:
        if clicking:
            controlador_raton.click(Button.left,1)
        time.sleep(0.001)
def caracteristicas_ventana():
    vent.geometry("120x60")
    vent.title("estado: apagado")
    vent.attributes('-topmost',1)
    vent.attributes('-toolwindow',1)   
    
    
tecla_elegida='t' #aqui esta la tecla asignada 

tecla_del_sistema=  KeyCode(char=tecla_elegida) 
clicking=False
controlador_raton= Controller()
monitor_de_tareas=threading.Thread(target=click_isquierdo)
monitor_de_tareas.start()

vent=tk.Tk()

def evento_al_pulsar(llave):
    if llave== tecla_del_sistema:
        global clicking
        clicking=not clicking

def cerrar_programa():
        global listener
        listener.stop()
        vent.title("estado: apagado")
        vent.destroy()
        
boton_apagar=tk.Button(vent,text="apagar",height=20,font="arial",command=cerrar_programa)

boton_apagar.pack(side="right",pady=5)
caracteristicas_ventana()
with Listener(on_press=evento_al_pulsar) as listener:
        vent.mainloop()
        listener.join()
