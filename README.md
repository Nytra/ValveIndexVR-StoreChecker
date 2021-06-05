# Valve Index VR - Store Availability Checker
A Python script which checks to see if the Valve Index VR hardware products are currently available on Steam

The script uses the `requests` and `bs4` Python packages to parse HTML from the Steam store to see if the Index VR products are available. You must install these with `pip` for the script to work.

You can use Windows Task Scheduler to make this script run at set intervals (eg: every 15 minutes) so that you will always be one of the first to know when the VR hardware becomes available.

There will be a loud and obnoxious beeping alarm that goes off if any of your desired products are available. There will be a total of thirty 1-second-duration tones with a 1-second-duration delay between them.

This program is quite rudimentary and was coded quickly. It will probably break if the HTML from the store ever changes. 

## Requirements

- Python 3.x

`pip install requests`

`pip install bs4`

- Windows operating system (for `winsound` library)

## Usage

`python.exe indexVrChecker.py` : execute the program normally

`python.exe indexVrChecker.py --nopause` : execute the program *without pausing at the end*

The script will check *only* for the products which are hard-coded in the `WANTED_ITEMS` list. These values are the indices [0-4] which correspond to the desired hardware. For example, an index of `1` corresponds to `'sku_partial_kit'` which is the HMD+Controller package. The hardware package names are defined in the `SKU_STRINGS` list. 

You *MUST* change the values in `WANTED_ITEMS` in order for this script to be useful to you.
