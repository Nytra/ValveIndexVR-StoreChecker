# Valve Index VR - Store Availability Checker
A Python script which checks to see if the Valve Index VR hardware products are currently available on Steam.

The script uses the `requests` and `bs4` (BeautifulSoup) Python packages to read HTML from the Steam store to see if the Index VR products are available. It also uses `simpleaudio` to play sound. You must install these with `pip` for the script to work.

You can use Windows Task Scheduler to make this script run at set intervals (e.g.: every 15 minutes) so that you will always be one of the first to know when the VR hardware becomes available.

There will be a loud and obnoxious alarm if any of your desired products are available. It will play the indexVrSfx.wav audio sample 30 times with a 1 second delay between each play.

The script will log the result of each check in the file `indexVrResults.dat`, in plain-text. You can use this file to look at previous results, just to make sure you didn't miss anything. 

The format of the log file is:

`Date[YYYY-MM-DD] Time[HH:MM:SS] ItemsChecked[CUR_N/MAX_N] ItemIndex[i=0-4] ItemName Result`

Log example:

`[2021-06-16] [16:50:35] 1/1 i=2 sku_hmd unavailable.`

## Requirements

- Python 3

Run these at command-line or terminal:

`pip install requests`

`pip install bs4`

`pip install simpleaudio`

## Usage

Extract contents of repository zipped file to a folder of your choice. Then open a terminal:

`python.exe indexVrChecker.py` : execute the program normally

`python.exe indexVrChecker.py --nopause` : execute the program *without pausing at the end*

`python.exe indexVrChecker.py --noalarm --checkall` : execute the program *without activating the alarm* and *check for all items*

`pythonw.exe indexVrChecker.py` : executes the program in the background (does not open console window, still makes sound)

---

The script will check *only* for the item id's which are hard-coded in the `WANTED_ITEMS` list. These values are the list indices [0-4], which correspond to the desired hardware. For example, an index of `1` corresponds to `'sku_partial_kit'` which is the HMD+Controller package. This list is ignored when `--checkall` is used.

Item Reference:

`0 : Full Kit`

`1 : HMD + Controllers Kit`

`2 : HMD Only`

`3 : Controllers Only`

`4 : Base Stations Only`
