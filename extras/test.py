import pyautogui
import time
pyautogui.FAILSAFE = True

time.sleep(2)

count = 0

for x in range(0, 500):
  pyautogui.press('down')
  count += 1

print(count)