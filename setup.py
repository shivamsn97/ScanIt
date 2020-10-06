import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scanit-cli", # Replace with your own username
    version="1.0.4",
    author="Shivam Saini",
    author_email="shivamsn97@gmail.com",
    description="Scan files for virus online using VirusTotal directly from your cli.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivamsn97/ScanIt/tree/module",
    packages=["scanit_cli"],
    license="MIT",
    install_requires = ["vt-py", "colorama"],
    entry_points='''
        [console_scripts]
        scanit=scanit_cli.scanit:main
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)