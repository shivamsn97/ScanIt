# ScanIt
Who keeps antivirus nowadays? Go on. Noone wants to slow down his PC AF for some unneccesory antivirus. But we sometimes needs to scan some file for virus. So here is an solution. ScanIt Scans a file using VirusTotal's online file scanner.

### NOTE: You are in `module` branch. For windows we suggest check out [master branch](https://github.com/shivamsn97/ScanIt/tree/master) too.

# Why ScanIt?
A lot of people, including me, prefers not to keep Antivirus in their PC. But sometimes we really need to scan a file for virus. At such times we use online virus scanners like VirusTotal.com. ScanIt has bring down this functionality to your cli, and guess what? It doesn't slows down your system by even a 0.01 percent. So its time to goodbye AntiViruses and say hello to online file scan services.

# Privacy?
The script first sends the hash of a file to VirusTotal to check if the same file is already available to VirusTotal. In this case your data is totally secure as the file is not uploaded. But if VirusTotal doesn't recognises that hash, then the script asks you if you want to upload the file, in case you answer with yes, it uploads the file. So it's up to you if you want to upload a file or not. Sensitive files should not be uploaded.

# Installation

### Installation from PyPi:

- Make sure you have python (version >= 3) and pip installed.
- Run the following command from your command line:

```bash
pip install scanit-cli  # may be pip3 in case of linux
```

### Installation from repo:

- Make sure you have `pip` and `git` installed. Now use the following commands to install scanit:
```bash
git clone https://github.com/shivamsn97/ScanIt
cd ScanIt
git checkout module
python setup.py install  # may be python3 in case of linux
```

#### Uninstallation:

- Run the following command:
```bash
pip uninstall scanit-cli  # May be pip3 in case of linux
```

# Notes
- Currently made only for Windows, contributions are welcome to make it work on linux too.
- Your privacy is in your hands. Please do not upload sensitive files to virustotal db.
- Please do not open low-efforts PR
- A star to the repo would be awesome.

# Credits
- <a target="_blank" href="https://icons8.com/icons/set/security-checked">Protect icon</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
