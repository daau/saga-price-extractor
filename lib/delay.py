# Globally installed packages
import pyautogui
import time
from termcolor import colored

LONG_DELAY_TIME = 0.25
SHORT_DELAY_TIME = 0.05

def long():
  time.sleep(LONG_DELAY_TIME)
  print("Long delay")

def short():
  time.sleep(SHORT_DELAY_TIME)
  print("short delay")
