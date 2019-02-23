# Globally installed packages
import pyautogui
import time
from termcolor import colored

SUPER_LONG_DELAY_TIME = 1
LONG_DELAY_TIME = 0.25
SHORT_DELAY_TIME = 0.05

def long():
  time.sleep(LONG_DELAY_TIME)

def super_long():
  time.sleep(SUPER_LONG_DELAY_TIME)

def short():
  time.sleep(SHORT_DELAY_TIME)
