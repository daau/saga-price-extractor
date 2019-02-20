# Globally installed packages
import pyautogui
import time
import pdb
from termcolor import colored

# Local packages
import delay
import vision

def focus_on_maplestory():
  print("Focusing on maplestory")
  pyautogui.click(400, 400)
  delay.long()

def open_fredrick():
  print("Opening frederick")
  pyautogui.moveTo(443, 258)
  pyautogui.doubleClick()

def open_price_check():
  print("Opening price check")
  pyautogui.moveTo(372, 374)
  pyautogui.click()

def open_link(x, y):
  pyautogui.moveTo(x, y)
  pyautogui.click()

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
  print("Opening chair")
  open_link(330, 357)

def open_etcs():
  print("Opening etcs")
  open_link(330, 376)  

def press_esc():
  pyautogui.press('esc')
  delay.long()

def go_to_nth_item(n):
  for x in range(0, n):
    pyautogui.press('down')
  pyautogui.press('enter')
  vision.wait_for_fredrick()
  pyautogui.press('space')

def press_down_n_times(times):
  for x in range(0, times):
    pyautogui.press('down')

def go_to_category(category):
  open_fredrick()
  vision.wait_for_fredrick()

  open_price_check()
  vision.wait_for_fredrick()

  if (category == "10%"):
    open_10_scroll()
  elif (category == "30%"):
    open_30_scroll()
  elif (category == "60%"): 
    open_60_scroll()
  elif (category == "70%"):
    open_70_scroll()
  elif (category == "100%"):
    open_100_scroll()
  elif (category == "chairs"):
    open_chair()
  elif (category == "etcs"):
    open_etcs()

def hide_mouse():
  pyautogui.moveTo(643, 261)

def remove_mouse():
  pyautogui.moveTo(55, 260)

delay.long()
press_down_n_times(146)