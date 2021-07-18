""" indexVrChecker.py: Program to check if the Valve Index VR products are in-stock on Steam

    Command-line args:
        --nopause : don't pause before program exit
        --noalarm : don't sound the alarm
        --checkall : check all sku purchase options

    Repository URL: https://github.com/Nytra/ValveIndexVR-StoreChecker

"""

from bs4 import BeautifulSoup
import requests
import datetime
from sys import argv
import time
import os

import simpleaudio

# === Globals and constants ===

HEADSET_URL = 'https://store.steampowered.com/app/1059530/Valve_Index_Headset/'

SKU_STRINGS = [
    'sku_full_kit',
    'sku_partial_kit',
    'sku_hmd',
    'sku_knuckles',
    'sku_bs'
]

# ===== DEFINE WHAT YOU WANT IN THE LIST BELOW =====

# (THESE MUST BE NUMBERS) (Uncomment the ones you want)

WANTED_ITEMS = [
    #0,
    #1,
    2,
    #3,
    #4
]

# Remember: 0=full_kit, 1=partial_kit, 2=hmd, 3=knuckles, 4=bases 

# ===== ===== ===== ===== ===== =====

def check_arg(arg):
    if len(argv) > 1 and arg in argv[1:]:
        return True
    return False

# Get path to script directory
scriptpath = os.path.realpath(__file__)
dirpath = os.path.split(scriptpath)[0]

# Attempt to load alarm sound effect
if not check_arg('--noalarm'):
    try:
        alert_sound_1 = simpleaudio.WaveObject.from_wave_file(dirpath + os.sep + "indexVrSfx.wav")
    except FileNotFoundError:
        print("error: unable to locate indexVrSfx.wav - alarm will be disabled.")
        alert_sound_1 = None
else:
    alert_sound_1 = None

# === Utility functions ===

def play_sound():
    if alert_sound_1 != None:
        alert_sound_1.play()

def check_available(btn_html, item_name):
    s = str(btn_html)

    if "Add to Cart" in s:
        print(item_name, 'IN STOCK!')
        return True

    elif "btn_disabled" in s:
        print(item_name, ':(')
        return False

    else:
        print(item_name, 'unknown status.')
        return -1

# === Main function ===

def main():
    r = requests.get(HEADSET_URL)

    soup = BeautifulSoup(r.content, 'html.parser')

    # stores sku purchase options as BeautifulSoup selected objects (ResultSet object)
    sku_arr = []

    # select the div relating to the sku purchase option - ex: 'div.valveindex_purchase_option.sku_full_kit'
    for i in range(len(SKU_STRINGS)):
        purchase_option = soup.select('div.valveindex_purchase_option.' + SKU_STRINGS[i])

        # check that it contains something
        if purchase_option:
            sku_arr.append(purchase_option)

    any_available = False
    items_checked = 0

    # loop for each item in sku_arr
    for i in range(len(sku_arr)):

        # select the 'Add to Cart' button from HTML (must select from [0] element of sku_arr)
        sku_btn = sku_arr[i][0].select('div.btn_addtocart')

        # check that this item is wanted
        if i in WANTED_ITEMS or check_arg('--checkall') == True:

            # check if available
            result = check_available(sku_btn, SKU_STRINGS[i])

            if result == True:
                any_available = True
            
            # error case
            if result == -1:
                print("Error:", SKU_STRINGS[i], "returned unknown status.")
                #input("press enter to continue.")

            # choose correct string for writing to log file
            if result == True:
                result_str = "IN STOCK."
            elif result == False:
                result_str = "unavailable."
            else:
                result_str = "error! unknown status."

            # open log file for writing (use append mode 'a')
            writefile = open(dirpath + os.sep + "indexVrResults.dat", "a")

            # log file format can be found in README.md from the GitHub repository
            writefile.write(f"[{now.date()}]" + " "\
                            + f"[{str(now.time()).split('.')[0]}]" + " "\
                            + f"{items_checked+1}/{int(len(WANTED_ITEMS) if check_arg('--checkall') == False else len(SKU_STRINGS))}" + " "\
                            + "i=" + str(i) + " "\
                            + SKU_STRINGS[i] + " "\
                            + result_str\
                            + "\n")

            # close file to free memory and resources
            writefile.close()

            if (result == True) and (check_arg('--noalarm') == False) and (alert_sound_1 != None):

                # make loud sounds obnoxiously to alert the user!
                print("ALARM ACTIVATING!")
                for _ in range(30):
                    play_sound()
                    time.sleep(1)
            
            # increment counter
            items_checked += 1

    # print newline, for visual style
    print()

    # if --nopause argument is used, quit program now
    if check_arg('--nopause') == True:

        quit()

        # failed test to create separate notification window (e.g. when script is running in background...)

        #if any_available or True:
            #play_sound()
            #subprocess.call(['python.exe', '-c', 'print(\'items are available!\');input(\'press enter to quit.\');'], creationflags=subprocess.CREATE_NEW_CONSOLE)
            #os.system("python.exe -c \"print('hello');input();\"")
            #pass
    else:

        # maybe create notification window here, too

        if any_available:
            print("Items are available! Pausing application.\n")
            input("Press enter to quit.")
            
        else:
            print("Nothing available. Sleeping for 3 seconds before exit.\n")
            time.sleep(3)

# === Program entry-point ===

if __name__ == "__main__":
    print("\nValve Index VR products Availability checker\n")
    now = datetime.datetime.now()
    print(now.date(), str(now.time()).split(".")[0])
    print()
    
    # it's useful to debug with play_sound() when running via pythonw.exe (no console window shown)
    #play_sound()

    # call main functions
    main()

# End of program.