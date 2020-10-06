# ScanIt
Who keeps antivirus nowadays? Go on. Noone wants to slow down his PC AF for some unneccesory antivirus. But we sometimes needs to scan some file for virus. So here is an solution. ScanIt Scans a file using VirusTotal's online file scanner.

# Why ScanIt?
A lot of people, including me, prefers not to keep Antivirus in their PC. But sometimes we really need to scan a file for virus. At such times we use online virus scanners like VirusTotal.com. ScanIt has bring down this functionality to your cli. You can even add it to your context menu using install.py as shown in image below, and guess what? It doesn't slows down your system by even a 0.01 percent. So its time to goodbye AntiViruses and say hello to online file scan services.

![Screenshot of ScanIt in context menu.](https://telegra.ph/file/edf19985aac281027e5d9.jpg)

# Privacy?
The script first sends the hash of a file to VirusTotal to check if the same file is already available to VirusTotal. In this case your data is totally secure as the file is not uploaded. But if VirusTotal doesn't recognises that hash, then the script asks you if you want to upload the file, in case you answer with yes, it uploads the file. So it's up to you if you want to upload a file or not. Sensitive files should not be uploaded.

# Installation
First make sure you have python (version >= 3) and pip installed in your system.

### For Linux Users:
- Linux users can use the [module branch](https://github.com/shivamsn97/ScanIt/tree/module) and install scanit-cli to use scanit.

- To install scanit-cli, use the following command:
```bash
pip3 install scanit-cli
```

### First, install the dependencies:
```shell
pip install -r requirments.txt 
```
### Now to create config.py, and adding to your context menu:
#### Automatic method (Recommended)
- Run the install.py script. Follow the on screen steps and you are done.

##### Uninstallation:
- Simply run uninstall.py

#### Manual method (Not at all recommended unless you are pro.)
- Rename sample-config.py to config.py
- Go to https://virustotal.com/, create an account, get an API key, and paste that api key in api_key variable in config.py
- Open Regestry Editor (In the start menu, search for regedit)
- Go to HKEY_CURRENT_USER > SOFTWARE > Classes > * > shell
- Right click on shell, create new key (new > key)
- Name it `ScanItbyShivam`
- In the DATA field for `(Default)` key, put data value: `Scan online with ScanIt`
- Right click on ScanItbyShivam, create new > String Value, Put name: `Icon` and Data value: `C:\Path\to\your\ScanIt\icon.ico` (Make sure to replace the path with the actual path)
- Right click on ScanItbyShivam, create new > key, rename it to `command`, in the data field for `(Default)`, put value: `"C:\Path\to\python\installation\python.exe" "C:\Path\to\your\ScanIt\." "%1"`
- Done

##### Uninstallation:
- Open Regestry Editor (In the start menu, search for regedit)
- Go to HKEY_CURRENT_USER > SOFTWARE > Classes > * > shell
- Right click on ScanItbyShivam, and delete it.
- Confirm deletation
- Done

# Notes
- Linux support is added in [module branch](https://github.com/shivamsn97/ScanIt/tree/module). Contributions are welcome.
- Your privacy is in your hands. Please do not upload sensitive files to virustotal db.
- Please do not open low-efforts PR
- A star to the repo would be awesome.

# Credits
- <a target="_blank" href="https://icons8.com/icons/set/security-checked">Protect icon</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
