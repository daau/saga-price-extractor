import pyautogui
import time

def focus_on_maplestory():
  pyautogui.click(400, 400)

def open_frederick():
  print("Opening frederick")
  time.sleep(0.5)
  pyautogui.moveTo(402, 140, duration=1)
  time.sleep(0.5)
  pyautogui.doubleClick()

def open_price_check():
  print("Opening price check")
  time.sleep(0.5)
  pyautogui.moveTo(372, 374, duration=1)
  time.sleep(0.5)
  pyautogui.click()

def open_category(x, y):
  time.sleep(0.5)
  pyautogui.moveTo(x, y, duration=1)
  time.sleep(0.5)
  pyautogui.click()

def open_10_scroll():
  print("Opening 10% scrolls")
  open_category(338, 248)

def open_30_scroll():
  print("Opening 30% scrolls")
  open_category(350, 266)

def open_60_scroll():
  print("Opening 60% scrolls")
  open_category(333, 283)

def open_70_scroll():
  print("Opening 70% scrolls")
  open_category(352, 302)

def open_100_scroll():
  print("Opening 100% scrolls")
  open_category(344, 319)

def open_chair():
  print("Opening 10% scrolls")
  open_category(330, 357)

def press_esc():
  time.sleep(0.5);
  pyautogui.press('esc')

def select_nth_item(n):
  print("hey")
  #n times press down arrow key
  # press enter
  # press space to skip text

  # START SCREENSHOTTING!

def is_scrollable():
  try:
    pyautogui.locateOnScreen('scroll.png',  region=(0,0, 800, 620))
  except Exception:
    return False
  else:
    return True

      

print("Working...")

# time.sleep(0.5)
# focus_on_maplestory()
# open_frederick()
# open_price_check()
# open_10_scroll()

print(is_scrollable())




print("Done")