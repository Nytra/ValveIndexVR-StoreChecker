# program to check if the Valve Index line of VR products are available on Steam

from bs4 import BeautifulSoup
import requests
import datetime
from sys import argv
import time
import winsound

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

def check_available(btn_html, item_name):
    s = str(btn_html)

    if "Add to Cart" in s:
        print(item_name, 'IN STOCK!')

        # make loud sounds obnoxiously to alert the user!
        print("ALARM ACTIVATING!")
        for _ in range(50):
            winsound.Beep(600, 1000)
            time.sleep(1)

        return True

    elif "btn_disabled" in s:
        print(item_name, ':(')
        return False

    else:
        print(item_name, 'unknown status.')
        return -1


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

    # for each purchase_option in sku_arr
    for i in range(len(sku_arr)):
        # select the 'Add to Cart' button
        sku_btn = sku_arr[i][0].select('div.btn_addtocart')

        if i in WANTED_ITEMS:
            # check if the purchase_option is available
            result = check_available(sku_btn, SKU_STRINGS[i])

            if result == True:
                any_available = True
            
            if result == -1:
                print("Error:", SKU_STRINGS[i], "returned unknown_status.")
                input("Press enter to continue.")

    # print newline, for nicer formatting in console :)
    print()

    # if --nopause argument is present, don't pause before exit

    if len(argv) > 1 and argv[1] == '--nopause':
        quit()
    else:
        if any_available:
            print("Items are available! Pausing application.\n")
            input("Press enter to quit.")
        else:
            print("Nothing available. Sleeping for 3 seconds before exit.")
            time.sleep(3)
            

if __name__ == "__main__":
    print("\nValve Index VR products Availability checker\n")
    now = datetime.datetime.now()
    print(now.date(), str(now.time()).split(".")[0])
    print()

    main()