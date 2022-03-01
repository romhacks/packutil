*Update 2022: We haven't had much time to work on this recently. We'll probably finish it. Eventually.*

# packutil
Packutil is a utility to easily set up a an environment where you can create resource packs for Minecraft: Java Edition.
It supports multiple versions and offers a simple GUI for configuration.

Packutil can currently create a working boilerplate pack with the default textures, but doesn't yet have an editing interface. It is considered alpha-quality software.

# Installation
Packaged binaries will be distributed for Windows and MacOS when milestone releases are made.
Linux users can run the python file directly.

# Requirements
## Binary builds

- Nothing

## Source
- Python 3 - Built against 3.10 but any recent should be fine
- Python packages - `pip3 install -r requirements.txt` or something similar will suffice

# Building binaries
If you'd like to make your own binaries of this software, it is confirmed to work with PyInstaller for Windows or py2app for MacOS.

## MacOS
- Requires `py2app` pip package.
1. `py2applet --make-setup packutil.py`
2. `python setup.py py2app` (Use `python3` if you have `python` aliased to v2)

The .app will be built to the `dist` folder.

## Windows
- Requires `pyinstaller` pip package.
1. `pyinstaller packutil.py`

The built program will be in the the `dist` folder.

Specifying `--onefile` will pack everything into one executable instead of generating a folder of support files.
