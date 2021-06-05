# Valve Index VR - Store Availability Checker
A Python script which checks to see if the Valve Index VR hardware products are currently available on Steam

The script uses `requests` and `BeautifulSoup` Python classes/libraries to parse HTML from the Steam store to see if the Index VR products are available.

You can use Windows Task Scheduler to make this script run at set intervals (eg: every 15 minutes) so that you will always be one of the first to know when the VR hardware becomes available.

This program is quite rudimentary and was coded quickly. It will probably break if the HTML from the store ever changes. 

## Usage

`python.exe indexVrChecker.py` : execute the program normally

`python.exe indexVrChecker.py --nopause` : execute the program *without pausing at the end*

The script will check \_*only*\_ for the products which are hard-coded in the WANTED_ITEMS list. These values are the indices [0-4] which correspond to the CSS selector for the desired hardware. For example, an index of `1` corresponds to `'sku_partial_kit'` which is the HMD+Controller package. The CSS selector strings are defined in the `SKU_STRINGS` list.
