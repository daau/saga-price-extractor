import pyautogui
import time

def print_one():
  print("one")

def print_two():
  print("two")

def print_three():
  print("three")

array = [print_one, print_two, print_three]

array[0]()