import threading
from pynput import keyboard
import pynput
#import time
from macros import revive, combo

     
def on_press(key):
        if key == pynput.keyboard.Key.delete:
            print('bot encerrado')
            return False
        
        if hasattr(key, 'char'):    
            if key.char == 'x':
                print("Tecla 'x' Pressionada")
                combo()

            if key.char == "'": #revive
                print("Tecla ''' Pressionada")
                revive()


with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()

