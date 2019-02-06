# Globally installed packages
import pyautogui
import time
import pdb
from termcolor import colored

# Local packages
import scroll
from category_scraper import CategoryScraper
import delay
import navigator

CATEGORIES = {
  "10%": 70,
  "30%": 57,
  "60%": 73,
  "70%": 37,
  "100%": 59,
  "chairs": 325
  # "etcs": 514
}

class Application:
  def __init__(self):
    self.category_scrapers = []
    self.setup()

  def setup(self):
    print("Setup")

    navigator.focus_on_maplestory()

    for key, value in CATEGORIES.items():
      print(f'Creating {key} scraper')
      self.category_scrapers.append(CategoryScraper(key, value))

  def scrape(self):
    for scraper in self.category_scrapers:
      scraper.scrape()

try:
  os.rmdir(../'export')
  program = Application().scrape()
except KeyboardInterrupt:
  print("\nProgram prematurely terminated.")

 