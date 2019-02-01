import pyautogui
import time

time.sleep(2)

print('Moving')

try:
  while True:
    time.sleep(2)
    print('Moving big')    
    pyautogui.scroll(-50)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)   
    pyautogui.scroll(-1)            
    time.sleep(2)
    print('Moving small')    
    pyautogui.scroll(-50)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    time.sleep(2)
    print('Moving small')    
    pyautogui.scroll(-50)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)
    pyautogui.scroll(-1)

except KeyboardInterrupt:
  print("\nDone.")