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

class Application:
  def __init__(self):
    print("Init")

  def call():
    print("call")


try:
 program = Application().call()
except KeyboardInterrupt:
  print("\nDone.")
