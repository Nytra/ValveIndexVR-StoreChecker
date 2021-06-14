# Valve Index VR - Store Availability Checker
A Python script which checks to see if the Valve Index VR hardware products are currently available on Steam.

The script uses the `requests` and `bs4` (BeautifulSoup) Python packages to read HTML from the Steam store to see if the Index VR products are available. It also uses `simpleaudio` to play sound. You must install these with `pip` for the script to work.

You can use Windows Task Scheduler to make this script run at set intervals (eg: every 15 minutes) so that you will always be one of the first to know when the VR hardware becomes available.

There will be a loud and obnoxious beeping alarm that goes off if any of your desired products are available. There will be a total of fifty 1-second-duration tones with a 1-second-duration delay between them. 

This program is quite basic and was coded quickly. It will probably break if the HTML from the store ever changes. It works for now, though.

This script was made for personal use. I test it a lot on my PC, and will continue to update it here whenever I fix bugs or add new features.

## Requirements

- Python 3.x.x

`pip install requests`

`pip install bs4`

`pip install simpleaudio`

## Usage

Extract contents of repository zipped file to a folder of your choice.

`python.exe indexVrChecker.py` : execute the program normally

`python.exe indexVrChecker.py --nopause` : execute the program *without pausing at the end*

`pythonw.exe indexVrChecker.py` : executes the program in the background (does not open console window, still makes sound)

The script will check *only* for the products which are hard-coded in the `WANTED_ITEMS` list. These values are the list indices [0-4] which correspond to the desired hardware. For example, an index of `1` corresponds to `'sku_partial_kit'` which is the HMD+Controller package.

You *MUST* change the values in `WANTED_ITEMS` in order for this script to be useful to you.

`0 : Full Kit`

`1 : HMD + Controllers Kit`

`2 : HMD Only`

`3 : Controllers Only`

`4 : Base Stations Only`
