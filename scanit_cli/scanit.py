import argparse
import os, sys
import hashlib, time
import time

def check_file_exists(given_path):
    if not os.path.isfile(given_path):
        raise argparse.ArgumentTypeError(f"{given_path} is not a valid file. Make sure you are trying to scan only file, not directory.")
    return given_path

def print_result(stats, file_path):
    print(colorama.Fore.MAGENTA)
    print("Scan Results for file named {}".format(file_path.split(os.sep)[-1]))
    print("-------------------------------------------------------"+colorama.Fore.RESET)
    for i in stats:
        print((colorama.Fore.RED if i in ["suspicious", "malicious"] else colorama.Fore.GREEN if i in ["harmless", "undetected"] else colorama.Fore.CYAN) + i + colorama.Fore.RESET + ": {}".format(stats[i]))
    print(colorama.Fore.MAGENTA + "-------------------------------------------------------")
    print("Verdict: \n" + colorama.Fore.RESET)
    num_safe = stats["harmless"] + stats["undetected"]
    num_unsafe = stats["suspicious"] + stats["malicious"]
    if num_unsafe == 0 and num_safe >= 20:
        print(colorama.Fore.GREEN + "TOTALLY SAFE" + colorama.Fore.RESET)
    elif num_unsafe == 0 and num_safe >=5:
        print(colorama.Fore.GREEN + "SAFE" + colorama.Fore.RESET)
    elif num_unsafe == 0 and num_safe:
        print(colorama.Fore.LIGHTGREEN_EX + "UNKNOWN" + colorama.Fore.RESET)
    elif num_unsafe == 0:
        print(colorama.Fore.YELLOW + "UNKNOWN" + colorama.Fore.RESET)
    elif num_safe > num_unsafe:
        print(colorama.Fore.LIGHTGREEN_EX + "UNKNOWN" + colorama.Fore.RESET)
    elif num_safe == 0:
        print(colorama.Fore.RED + "VERY UNSAFE" + colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "UNSAFE" + colorama.Fore.RESET)
    print(colorama.Fore.MAGENTA + "-------------------------------------------------------" + colorama.Fore.RESET)
    

dir_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(dir_path, "config.py")

try:
    import vt
    import colorama
except ModuleNotFoundError:
    try:
        import pip
        print("All requirements are not satisfies. ")
        choice = input("Do you want to install all the requirements now using pip? (Y/N): ")
        if choice.lower() in ["y", "yes"]:
            os.system(sys.executable + " -m pip install vt-py colorama")
        else:
            print("Installation cancelled.")
            time.sleep(2)
            exit()
    except ModuleNotFoundError:
        print("All requirements are not installed and you don't have pip installed. Please either install pip, or install all the requirements manually.")
    import vt
    import colorama


try:
    sys.path.append(dir_path)
    import config
except ModuleNotFoundError:
    print("Needs to generate config file first.")
    input("Press enter to continue.")
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
    import config

API_KEY = config.api_key

def main():
    if os.name == "nt":
        colorama.init(convert=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Path of the file you want to scan.", type=check_file_exists)
    args = parser.parse_args()
    file_path = args.filepath

    print("Calculating Hash.", end="")
    with open(file_path,"rb") as f:
        # bytes = f.read() # read entire file as bytes
        # file_hash = hashlib.sha256(bytes).hexdigest()
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    file_hash = file_hash.hexdigest()

    with vt.Client(API_KEY) as client:
        try:
            print("\rChecking if file already available in VirusTotal DB.", end="")
            stats = client.get_object("/files/{}".format(file_hash)).last_analysis_stats
            print("\rFile is already available in VirusTotal DB.         ")
        except vt.error.APIError as ex:
            if not ex.code == "NotFoundError":
                raise
            with open(file_path, "rb") as f:
                choice = input("\rFile not available in VirusTotal DB. Do you want to upload? (Internet charges may apply) (Y/N)\n :: ")
                if choice.lower() in ["y", "yes"]:
                    print(colorama.Fore.GREEN + "Now Uploading. ")
                    analysis = client.scan_file(f)
                    while True:
                        analysis = client.get_object("/analyses/{}".format(analysis.id))
                        print("\r" + colorama.Fore.MAGENTA +  "Current Status: " + colorama.Fore.RESET + analysis.status, end="")
                        if analysis.status == "completed":
                            break
                        time.sleep(10)
                    stats = analysis.stats
                else:
                    print("Operation cancelled. ")
                    time.sleep(2)
                    exit()

        print_result(stats, file_path)
        #input("Press enter to exit...")

if __name__ == "__main__":
    main()