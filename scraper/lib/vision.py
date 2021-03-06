# Globally installed packages
import pdb
import pyautogui
import time
from termcolor import colored
import pytesseract
from PIL import Image

# Local packages
import delay
import navigator

# Config
TESSERACT_CONFIG = '--psm 6'

def wait_for_fredrick():
  for attempt in range(6):
    try:
      delay.short()
      pyautogui.locateOnScreen("./images/fredrick.png", region=(100, 200, 300, 300), confidence = 0.8)
    except: Exception
    else:
      break

def find_based_on():
  coords = pyautogui.locateOnScreen("./images/based.png", region=(288, 184, 337, 241), confidence=0.6)
  return coords

def find_here_are():
  coords = pyautogui.locateOnScreen("./images/here.png", region=(288, 184, 337, 241), confidence=0.6)
  return coords

def find_purchases():
  coords = pyautogui.locateOnScreen("./images/purchases.png", region=(288, 184, 337, 241), confidence = 0.83)
  return coords

def find_ok():
  coords = pyautogui.locateOnScreen("./images/ok.png", region=(606, 391, 80, 122), confidence = 0.83)
  return coords  

def get_image_of_entry():
  here_tuple = find_here_are()
  based_tuple = find_based_on()

  X = here_tuple.left
  Y = here_tuple.top + 16

  width = (based_tuple.left - here_tuple.left) + 1
  if (width < 10):
    width = 300
  height = 16
  
  return pyautogui.screenshot(region=(X,Y, width, height))

def get_text_from_image(image):
  return pytesseract.image_to_string(image, config=TESSERACT_CONFIG)

def get_name_of_entry():
  navigator.hide_mouse()
  image = resize(get_image_of_entry())
  return get_text_from_image(image)

def take_full_screenshot():
  navigator.hide_mouse()
  return pyautogui.screenshot(region=(290, 183, 334, 240))

def take_zoned_screenshot():
  navigator.hide_mouse()
  purchases_tuple = find_purchases()
  ok_tuple = find_ok()

  # X start = 290
  # Y distance between purchases and start of entries = 30
  X = 290
  Y = (purchases_tuple.top + 29)

  # Width = 350
  # Y distance between OK and bottom border = 30  
  width = 338
  height = (ok_tuple.top - 30) - Y

  return pyautogui.screenshot(region=(X, Y, width, height))

def resize(image):
  SCALE_FACTOR = 2

  size = image.width*SCALE_FACTOR, image.height*SCALE_FACTOR
  return image.resize(size, Image.ANTIALIAS)

def is_scrollable():
  try:
    pyautogui.locateOnScreen('./images/scroll.png',  region=(138, 164, 520, 314), confidence = 0.8)
  except Exception:
    return False
  else:
    return True

def can_still_scroll():
  try:
    pyautogui.locateOnScreen('./images/scroll_bottom.png', region=(587, 363, 119, 98), confidence=0.8)
  except Exception:
    return True # Scrollbar not found.. can still scroll
  else:
    return False # Scrollbar found.. can't scroll


# ==========================
# DEBUGGING
# ==========================