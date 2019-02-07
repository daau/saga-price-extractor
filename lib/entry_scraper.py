# Globally installed packages
import pyautogui
import time
import pdb
import os
from termcolor import colored

# Local packages
import navigator
import vision
import scroll
from writer import Writer

class EntryScraper():
  def __init__(self, n, parent_dirs):
    self.name = None
    self.n = n # Represents nth entry in category.. used for filename
    self.parent_dirs = parent_dirs
    self.directory = None
    self.count = 0
    self.writer = None

  def scrape(self):
    self.create_directory()
    self.visit_item()
    self.get_name_of_entry()
    self.save_name_of_entry()
    self.take_screenshots_of_entries()
    print("Done!")
    navigator.press_esc()

  def create_directory(self):
    self.directory = f"../export/{self.parent_dirs}/{self.n}"
    os.makedirs(self.directory)
    self.writer = Writer(self.directory + f"/data.txt")

  def visit_item(self):
    vision.wait_for_fredrick()
    navigator.go_to_nth_item(self.n)
    navigator.remove_mouse()

  def get_name_of_entry(self):
    vision.wait_for_fredrick()
    self.name = vision.get_name_of_entry()
    print(f'Getting prices for {self.name}')

  def save_name_of_entry(self):
    f = Writer(self.directory + "/name.txt")
    f.write(self.name)
    f.save()

  def take_screenshots_of_entries(self):
    if(vision.is_scrollable()):
      image = vision.resize(vision.take_zoned_screenshot())
      text = vision.get_text_from_image(image)
      self.writer.write(text)
      scroll.big()

      count = 1
      scroll_pattern = [scroll.big, scroll.small, scroll.small]

      while(True):
        if(not vision.can_still_scroll()):
          break
        image = vision.resize(vision.take_full_screenshot())
        text = vision.get_text_from_image(image)
        self.writer.write(text)

        scroll_pattern[count]()
        count += 1
        if (count == 3):
          count = 0

    else:
      image = vision.resize(vision.take_zoned_screenshot())
      text = vision.get_text_from_image(image)
      self.writer.write(text)
      self.writer.save()