# Globally installed packages
import pyautogui
import time
from termcolor import colored

# Local packages
import delay
import navigator
import vision
import scroll

class EntryScraper():
  def __init__(self, n):
    self.name = None
    self.n = n

  def scrape(self):
    self.visit_item()
    self.get_name_of_entry()
    self.take_screenshots_of_entries()

  def visit_item(self):
    navigator.go_to_nth_item(self.n)

  def get_name_of_entry(self):
    self.name = vision.get_name_of_entry()
    print(f'Getting prices for {self.name}')

  def take_screenshots_of_entries():
    if(vision.is_scrollable()):
      print("yey")
    else:
      print("oh no")
