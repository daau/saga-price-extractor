# Globally installed packages
import pyautogui
import time
from termcolor import colored

# Local packages
import delay

def scroll_nth_lines(n):
  pyautogui.scroll(-50)
  for x in range(0, n):
    pyautogui.scroll(-1)
  delay.long()

def big():
  scroll_nth_lines(6)

def small():
  scroll_nth_lines(5)

delay.long()
big()
small()
small()