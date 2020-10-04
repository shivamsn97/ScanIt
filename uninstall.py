import winreg
import os, sys, time

if sys.version_info[0] < 3:
    print("Python 2 is not supported. Please use python 3.")
    time.sleep(2)
    exit()

if os.name != "nt":
    print("Only Windows is supported.")
    time.sleep(2)
    exit()


def deleteSubkey(key0, key1, key2=""):
    if key2=="":
        currentkey = key1
    else:
        currentkey = key1+ "\\" +key2

    open_key = winreg.OpenKey(key0, currentkey ,0,winreg.KEY_ALL_ACCESS)
    infokey = winreg.QueryInfoKey(open_key)
    for _ in range(0, infokey[0]):
        #NOTE:: This code is to delete the key and all subkeys.
        #  If you just want to walk through them, then 
        #  you should pass x to EnumKey. subkey = winreg.EnumKey(open_key, x)
        #  Deleting the subkey will change the SubKey count used by EnumKey. 
        #  We must always pass 0 to EnumKey so we 
        #  always get back the new first SubKey.
        subkey = winreg.EnumKey(open_key, 0)
        try:
            winreg.DeleteKey(open_key, subkey)
        except:
            deleteSubkey( key0, currentkey, subkey )
            # no extra delete here since each call 
            #to deleteSubkey will try to delete itself when its empty.

    winreg.DeleteKey(open_key,"")
    open_key.Close()
    return

choice = input("Are you sure you want to remove ScanIt from windows context menu? (Y/N) : ")
if choice.lower() in ["y", "yes"]:
    deleteSubkey(winreg.HKEY_CURRENT_USER, "software\\Classes\\*\\Shell\\ScanItbyShivam")
    print("Done. Successfully removed ScanIt from your device.")
    time.sleep(2)
    exit()