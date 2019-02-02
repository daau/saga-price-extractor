# Globally installed packages
import pdb
import pyautogui
import time
from termcolor import colored

# Local packages
import delay

def wait_for_frederick():
  print("Waiting for Fredrick...")
  loop = True
  while loop:
    try: 
      pyautogui.locateOnScreen("./images/fredrick.png", region=(100, 200, 300, 300))
    except: Exception
    else: 
      loop = False
  print("Found!")

def find_based_on():
  coords = pyautogui.locateOnScreen("./images/based.png", region=(288, 184, 337, 241), confidence=0.6)
  print(coords)
  return coords

def find_here_are():
  coords = pyautogui.locateOnScreen("./images/here.png", region=(288, 184, 337, 241), confidence=0.6)
  print(coords)
  return coords

def get_name_of_entry():
  here_tuple = find_here_are()
  based_tuple = find_based_on()

  X = here_tuple.left
  Y = here_tuple.top + 16

  width = (based_tuple.left - here_tuple.left) + 1
  height = 16
  
  image = pyautogui.screenshot(region=(X,Y, width, height))
  image.save("test.png")

get_name_of_entry()

def take_full_screenshot(count):
  pyautogui.screenshot(f"./export/{count}.png", region=(290, 189, 334, 234))

def get_prices():
  if is_scrollable():
    scroll_and_take_screenshots()
  else:
    take_zoned_screenshot()

def take_zoned_screenshot():
  return 1
  # TBA

def scroll_and_take_screenshots():
  count = 0
  pattern = [scroll.big, scroll.small, scroll.small]
  while can_still_scroll():
    pattern[count]()
    count += 1
    if (count == 2):
      count = 0


def is_scrollable():
  try:
    pyautogui.locateOnScreen('scroll.png',  region=(0,0, 800, 620))
  except Exception:
    return False
  else:
    return True

def can_still_scroll():
  try:
    pyautogui.locateOnScreen('someButton.png', region=(624, 388, 21, 29))
  except Exception:
    return True # Scrollbar not found.. can still scroll
  else:
    return False # Scrollbar found.. can't scroll