# Saga Price Extractor
This repository consists of two programs: a bot and a data cleaner. The programs are intended for use with MapleSaga, a private, pre-Big Bang MapleStory server.

## The bot
The bot is used to extract data from a game. Specifically, this bot extracts free market data from Frederick, an NPC in MapleSaga. 

The bot is written in written in Python and relies heavily on pyautogui, a GUI automation library.

If you'd like to use the bot, you must install the following:

1. pyautogui (Python library)
2. Pillow (Python library)
3. pytesseract (Python library)
4. Tesseract (OCR)

You must also calibrate the following

1. Scroll speed in the `scroll` module
2. Coordinates of various Fredrick links in the `navigator` module
3. Coordinates of GUI elements in the `vision` module

## The cleaner
The cleaner is written in Ruby. The cleaner takes the raw data from the scraper and performs a variety of tasks:

1. Strips the raw data of any superfluos information
2. Ensures entry names are correct
3. Removes duplicate entries (Fredrick lists several)
4. Removes erroneous entries (again, Fredrick lists several)
5. Exports the data as JSON

To ensure correctness for item names, the cleaner cross references extracted raw data names against a list of verified correct entry names, which is available from [sagasquare.](sagasquare.com) Obtaining the list of correct item names from sagasquare is necessary, as the official MapleSaga library is incomplete and contains many errors.

To use the cleaner, you must have the `fuzzy_match` gem installed.

## Data
If you're just interested in the raw data, please check out `./cleaner/fredrick_data.json`