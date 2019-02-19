import pyautogui
import time
import pdb
import pytesseract
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

pyautogui.FAILSAFE = True

image = pyautogui.screenshot(region=(290, 183, 334, 240))
size = image.width*2, image.height*2
new_image = image.resize(size, Image.ANTIALIAS)
pdb.set_trace()
print("hey")