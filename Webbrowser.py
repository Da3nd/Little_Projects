import pyautogui
import time
import keyboard
import pyperclip

lt = ['youtube.com', 'google.com', 'chess.com', 'pinterest.com', 'github.com']
dm = 'https://www.'
pyautogui.FAILSAFE=False

while not keyboard.is_pressed('q'):
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            pressed = event.name


            if pressed.isdigit() and int(pressed) in range(1,6):
                url = f'{dm}{lt[int(pressed)-1]}'
                
                pressed = int(pressed)
                pyperclip.copy(url)
                print(url)
            
                keyboard.send('win+r')
                time.sleep(0.1)
                           
                keyboard.send("ctrl+v")
                keyboard.send('enter')
                    
            else:
                print('HELL NAHH, WATYA DOIN??')
