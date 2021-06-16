# program to check if the Valve Index line of VR products are available on Steam

#   command-line args:
#       --nopause : don't pause before program exit
#       --noalarm : don't sound the alarm
#       --checkall : check all sku purchase_options

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

scriptpath = os.path.realpath(__file__)
dirpath = os.path.split(scriptpath)[0]

alert_sound_1 = simpleaudio.WaveObject.from_wave_file(dirpath + os.sep + "indexVrSfx.wav")

# === End of Globals and constants ===

# === Utility functions ===

def play_sound():
    alert_sound_1.play()

def check_arg(arg):
    if len(argv) > 1 and arg in argv[1:]:
        return True
    return False

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

# === End of Utility functions ===

# === Main function ===

def main():
    r = requests.get(HEADSET_URL)

    soup = BeautifulSoup(r.content, 'html.parser')

    # stores sku purchase_options as BeautifulSoup selected objects (ResultSet object)
    sku_arr = []

    # select the div relating to the sku option. ex: 'div.valveindex_purchase_option.sku_full_kit'
    for i in range(len(SKU_STRINGS)):
        purchase_option = soup.select('div.valveindex_purchase_option.' + SKU_STRINGS[i])
        if purchase_option:
            sku_arr.append(purchase_option)

    any_available = False
    items_checked = 0

    # for each purchase_option in sku_arr
    for i in range(len(sku_arr)):

        # select the 'Add to Cart' button
        sku_btn = sku_arr[i][0].select('div.btn_addtocart')

        if i in WANTED_ITEMS or check_arg('--checkall') == True:

            # check if the purchase_option is available
            result = check_available(sku_btn, SKU_STRINGS[i])

            if result == True:
                any_available = True
            
            if result == -1:
                print("Error:", SKU_STRINGS[i], "returned unknown_status.")
                #input("Press enter to continue.")

            if result == True:
                result_str = "IN STOCK."
            elif result == False:
                result_str = "unavailable."
            else:
                result_str = "error! unknown status."

            writefile = open(dirpath + os.sep + "indexVrResults.dat", "a")

            writefile.write(f"[{now.date()}] [{str(now.time()).split('.')[0]}]" + " "\
                            + f"{items_checked+1}/{int(len(WANTED_ITEMS) if check_arg('--checkall') == False else len(SKU_STRINGS))}" + " "\
                            + "i=" + str(i) + " "\
                            + SKU_STRINGS[i] + " "\
                            + result_str\
                            + "\n")

            writefile.close()

            if result == True and check_arg('--noalarm') == False:

                # make loud sounds obnoxiously to alert the user!
                print("ALARM ACTIVATING!")
                for _ in range(30):
                    play_sound()
                    time.sleep(1)
            
            items_checked += 1

    # print newline, for nicer formatting in console :)
    print()

    # if --nopause argument is present, don't pause before exit
    if check_arg('--nopause') == True:

        # trying to spawn a new info message window (unfinished test...)
        #if any_available or True:
            #play_sound()
            #subprocess.call(['python.exe', '-c', 'print(\'items are available!\');input(\'press enter to quit.\');'], creationflags=subprocess.CREATE_NEW_CONSOLE)
            #os.system("python.exe -c \"print('hello');input();\"")
            #pass

        quit()
    else:

        # if any wanted items are available, spawn a new visible console window and tell the user via print() text, then pause until the user closes it.
        # (not implemented)

        if any_available:
            print("Items are available! Pausing application.\n")
            input("Press enter to quit.")
            
        else:
            print("Nothing available. Sleeping for 3 seconds before exit.\n")
            time.sleep(3)

    #play_sound()

# === End of main function ===

# === Program entry-point ===

if __name__ == "__main__":
    print("\nValve Index VR products Availability checker\n")
    now = datetime.datetime.now()
    print(now.date(), str(now.time()).split(".")[0])
    print()
    
    # it's useful to debug with play_sound() when running via pythonw.exe (no console window shown)
    #play_sound()

    main()

# End of program entry-point, and End of program.