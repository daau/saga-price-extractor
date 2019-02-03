# Globally installed packages
import pyautogui
import time
from termcolor import colored

# Local packages
import scroll
import delay
import scroll
import visual

def focus_on_maplestory():
  pyautogui.click(400, 400)
  delay.short()

def open_fredrick():
  print("Opening frederick")
  pyautogui.moveTo(443, 258)
  pyautogui.doubleClick()

def open_price_check():
  print("Opening price check")
  pyautogui.moveTo(372, 374)
  pyautogui.click()
  delay.long()

def open_link(x, y):
  pyautogui.moveTo(x, y)
  pyautogui.click()
  delay.long()

def open_10_scroll():
  print("Opening 10% scrolls")
  open_link(338, 248)

def open_30_scroll():
  print("Opening 30% scrolls")
  open_link(350, 266)

def open_60_scroll():
  print("Opening 60% scrolls")
  open_link(333, 283)

def open_70_scroll():
  print("Opening 70% scrolls")
  open_link(352, 302)

def open_100_scroll():
  print("Opening 100% scrolls")
  open_link(344, 319)

def open_chair():
  print("Opening 10% scrolls")
  open_link(330, 357)

def press_esc():
  pyautogui.press('esc')
  delay.long()

def go_to_nth_item(n):
  for x in range(0, n):
    pyautogui.press('down')
  pyautogui.press('enter')
  delay.long() # Wait for fredrick
  pyautogui.press('space')

  # START SCREENSHOTTING!s

def press_down_n_times(times):
  for x in range(0, times):
    pyautogui.press('down')
    time.sleep(FAST_SLEEP_TIME)

def go_to_category(category):
  open_fredrick()
  open_price_check()
  if (category == "10% scroll"):
    open_10_scroll()
  elif (category == "30% scroll"):
    open_30_scroll()
  elif (category == "60% scroll"): 
    open_60_scroll()
  elif (category == "70% scroll"):
    open_70_scroll()
  elif (category == "100% scroll"):
    open_100_scroll()
  elif (category == "chair"):
    open_chair()
  delay.long()

time.sleep(3)
go_to_nth_item(10)