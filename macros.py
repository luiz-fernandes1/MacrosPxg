import pyautogui
from pynput import keyboard, mouse
import time

list_hotkeys_attack = [{"hotkey": 'F1', "delay": 0.6},
                       {"hotkey": 'F2', "delay": 0.6}, 
                       {"hotkey": 'F3', "delay": 0.6}, 
                       {"hotkey": 'F4', "delay": 0.6}, 
                       {"hotkey": 'F5', "delay": 0.6}]

def revive():
    original_position = pyautogui.position()
    new_position = (21, 37); 
    pyautogui.moveTo(new_position[0], new_position[1])

    mouse_controller.click(mouse.Button.right, 1)
    print("clicando")
    time.sleep(0.3)

    keyboard_controller.press(keyboard.Key.shift)
    keyboard_controller.press(keyboard.Key.f2)
    keyboard_controller.release(keyboard.Key.f2)
    keyboard_controller.release(keyboard.Key.shift)
    print("batendo revive")
    time.sleep(0.3)

    mouse_controller.click(mouse.Button.right, 1)
    print("tirando o poke da ball")

    pyautogui.moveTo(original_position[0], original_position[1])

def combo():
    try:
        keyboard_controller.press(keyboard.Key.alt)
        keyboard_controller.press('1')
        keyboard_controller.release('1')
        keyboard_controller.release(keyboard.Key.alt)
        print("Alt + 1 pressionado e liberado")
        time.sleep(0.1)
        
        keyboard_controller.press(keyboard.Key.f1)
        keyboard_controller.release(keyboard.Key.f1)
        print("F1 pressionado e liberado")
        time.sleep(0.6)
        
        keyboard_controller.press(keyboard.Key.f2)
        keyboard_controller.release(keyboard.Key.f2)
        print("F2 pressionado e liberado")
        time.sleep(0.6)
        
        keyboard_controller.press(keyboard.Key.f3)
        keyboard_controller.release(keyboard.Key.f3)
        print("F3 pressionado e liberado")
        time.sleep(0.6)
        
        keyboard_controller.press(keyboard.Key.f4)
        keyboard_controller.release(keyboard.Key.f4)
        print("F4 pressionado e liberado")
        time.sleep(0.6)
        
        keyboard_controller.press(keyboard.Key.f5)
        keyboard_controller.release(keyboard.Key.f5)
        print("F5 pressionado e liberado")
        time.sleep(0.6)
        
    
    except AttributeError:
        pass

keyboard_controller = keyboard.Controller()
mouse_controller = mouse.Controller()