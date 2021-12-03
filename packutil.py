# packutil authored by team electronika
import zipfile
import PySimpleGUI as sg
from black import sys
import src.packInitSetup as iSetup
import src.web as web
import os
from zipfile import ZipFile

sg.theme("DarkPurple1")


def ControlledExit(reason=None):
    if reason == None:
        sg.Window(
            "Packutil is exiting",
            [
                [sg.Text("Packutil is exiting.")],
                [sg.Button("OK")],
            ],
        ).read(close=True)
    else:
        sg.Window(
            "Packutil is exiting",
            [
                [sg.Text("Packutil is exiting for the following reason:")],
                [sg.Text(reason)],
                [sg.Button("OK")],
            ],
        ).read(close=True)
    sys.exit(1)


event, values = sg.Window(
    "Welcome to packutil",
    [
        [sg.Text("Choose an existing project folder or make a new one.")],
        [sg.Button("Existing"), sg.Button("New")],
    ],
).read(close=True)

if event == None:
    ControlledExit("Project load was cancelled.")

folder = sg.popup_get_folder("Choose a project folder")
if folder == None:
    ControlledExit("Folder choosing was cancelled.")

if event == "Existing":
    if not os.path.exists(f"{folder}/pack.mcmeta"):
        sg.popup(
            "This folder isn't set up for a Resource Pack. Try using the 'New' option."
        )
else:
    iSetup.InitSetup(folder)

sg.popup(
    "Packutil will now download the default textures for modification. This could take a little while."
)

if not os.path.exists("textures"):
    os.mkdir("textures")
    web.GUIDownloadFile("https://romhacks.github.io/textures.zip", "textures/textures.zip")
    with ZipFile("textures/textures.zip", "r") as zipFile:
        total = len(zipFile.namelist())
        updateProg = 1
        for file in zipFile.namelist():
            updateProg += 1
            if updateProg == 500:
                sg.one_line_progress_meter(
                    "Texture Extract",
                    zipFile.namelist().index(file),
                    total,
                    "Extracting textures, please be patient",
                    no_button=True,
                )
                updateProg = 1
            zipFile.extract(file, "textures")
        sg.one_line_progress_meter(
            "Texture Extract",
            total,
            total,
            "Extracting textures, please be patient",
            no_button=True,
        )
    os.remove("textures/textures.zip")
    sg.popup("Default textures have been downloaded.")

