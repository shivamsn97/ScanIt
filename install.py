import os, sys, time

if sys.version_info[0] < 3:
    print("Python 2 is not supported. Please use python 3.")
    time.sleep(2)
    exit()

dir_path = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.join(dir_path, ".")
icon_path = os.path.join(dir_path, "icon.ico")
python_path = sys.executable
config_path = os.path.join(dir_path, "config.py")

if os.name != "nt":
    print("Only Windows is supported. For linux, you can use the 'module' branch, https://github.com/shivamsn97/ScanIt/tree/module")
    time.sleep(2)
    exit()

try:
    import vt
    import colorama
except ModuleNotFoundError:
    print("Please install required modules first using command: ")
    print("  > pip install -r requirements.txt")
    time.sleep(2)
    exit()

try:
    sys.path.append(dir_path)
    import config
except ModuleNotFoundError:
    print("Needs to generate config file first. ")
    vt_url = "https://www.virustotal.com/gui/home"
    print("Please follow the following steps carefully: ")
    try:
        import webbrowser
        webbrowser.open(vt_url)
        print("1. Your browser is opened for VirusTotal HomePage. ")
    except:
        print("1. Open this page in your browser: {}".format(vt_url))
    print("   - In the top right corner, click on sign up (or sign in if you already have an account), and follow steps accordingly to create (or login to) your account")
    print("   (In case you created an account, check your email for a confirmation message and activte your account)")
    print("2. In the top right corner, click on your Name with profile icon, click on API Key, copy your personal API Key, and paste it here (Just right click on the terminal after copying.)")
    API_KEY = input("Paste API key :: ").strip()
    while not API_KEY:
        API_KEY = input("Something went wrong. Paste API key :: ").strip()
    try:
        with vt.Client(API_KEY) as client:
            file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")
    except vt.error.APIError as ex:
        if ex.code == "WrongCredentialsError":
            print("The API Key you entered is Invalid. Exiting...")
            time.sleep(3)
            exit()
    with open(config_path, "w") as fl:
        fl.write("api_key = '{}'".format(API_KEY))
    print("Done. Created config.py")


import winreg

def define_action_on(filetype, registry_title, command, title=None, icon = None):
    """
    define_action_on(filetype, registry_title, command, title=None)
        filetype: either an extension type (ex. ".txt") or one of the special values ("*" or "Directory"). Note that "*" is files only--if you'd like everything to have your action, it must be defined under "*" and "Directory"
        registry_title: the title of the subkey, not important, but probably ought to be relevant. If title=None, this is the text that will show up in the context menu.
    """
    #all these opens/creates might not be the most efficient way to do it, but it was the best I could do safely, without assuming any keys were defined.
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Classes", 0, winreg.KEY_SET_VALUE)
    k1 = winreg.CreateKey(reg, filetype) #handily, this won't delete a key if it's already there.
    k2 = winreg.CreateKey(k1, "shell")
    k3 = winreg.CreateKey(k2, registry_title)
    k4 = winreg.CreateKey(k3, "command")
    if title != None:
        winreg.SetValueEx(k3, None, 0, winreg.REG_SZ, title)
    if icon != None:
        winreg.SetValueEx(k3, "Icon", 0, winreg.REG_SZ, icon)
    winreg.SetValueEx(k4, None, 0, winreg.REG_SZ, command)
    winreg.CloseKey(k3)
    winreg.CloseKey(k2)
    winreg.CloseKey(k1)
    winreg.CloseKey(reg)




choice = input("Are you sure you want to install ScanIt to your device? (Y/N): ")
if choice.lower() in ["y", "yes"]:
    define_action_on("*", "ScanItbyShivam", "\"{}\" \"{}\" \"%1\"".format(python_path, script_path), "Scan online with ScanIt", icon_path)
    print("Done. Succesfully installed ScanIt. \nPlease Don't remove or move this directory to somewhere else without uninstalling first.\n\nPress enter to exit. ")
    input()
    exit()