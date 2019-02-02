# Globally installed packages
import pyautogui
import time
from termcolor import colored

# Local packages
import scroll
import category_scraper
import delay
import entry_scraper
import navigator
import scroll
import visual

def focus_on_maplestory():
  pyautogui.click(400, 400)
  delay.short()

def open_frederick():
  print("Opening frederick")
  pyautogui.moveTo(443, 258)
  pyautogui.doubleClick()
  delay.long()

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

def select_nth_item(n):
  print("hey")
  #n times press down arrow key
  # press enter
  # press space to skip text

  # START SCREENSHOTTING!s

def press_down_n_times(times):
  for x in range(0, times):
    pyautogui.press('down')
    time.sleep(FAST_SLEEP_TIME)

def go_to_item(item):
  open_frederick()
  open_price_check()
  if (item == "10% scroll"):
    open_10_scroll()
  elif (item == "30% scroll"):
    open_30_scroll()
  elif (item == "60% scroll"): 
    open_60_scroll()
  elif (item == "70% scroll"):
    open_70_scroll()
  elif (item == "100% scroll"):
    open_100_scroll()
  elif (item == "chair"):
    open_chair()
  delay.long()

def get_nth_item(n):
  press_down_n_times(n)

  pyautogui.press('enter')
  delay.long()
  pyautogui.press('space')
  delay.long()

