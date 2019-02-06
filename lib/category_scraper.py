# Globally installed packages
import pyautogui
import pdb

# Local packages
import delay
import navigator
from entry_scraper import EntryScraper

class CategoryScraper():
  def __init__(self, name, number_of_entries):
    self.name = name
    self.number_of_entries = number_of_entries
    self.entry_scrapers = []

    self.setup()

  def setup(self):
    for i in range(self.number_of_entries):  
      self.entry_scrapers.append(EntryScraper(i))
  
  def visit_category(self):
    navigator.go_to_category(self.name)


  def scrape(self):
    for scraper in self.entry_scrapers:
      navigator.go_to_category(self.name)
      scraper.scrape


# ==========================
# DEBUGGING
# ==========================

# navigator.focus_on_maplestory()
# CategoryScraper("10%", 10).visit_category()