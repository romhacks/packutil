# packutil authored by team electronika
import PySimpleGUI as sg
from src.fileOp import GUIFileCopy
import src.packInitSetup as iSetup
import src.web as web
import os
import sys
from zipfile import ZipFile

sg.theme("DarkPurple1")


def ControlledExit(reason=None):  # exit while notifying user
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


if not os.path.exists(
    "textures"
):  # checks if textures exists- if not download and extract them
    sg.popup(
        "Packutil will now download the default textures for modification. This could take a little while."
    )
    os.mkdir("textures")
    web.GUIDownloadFile(
        "https://romhacks.github.io/textures.zip", "textures/textures.zip"
    )
    with ZipFile("textures/textures.zip", "r") as zipFile:
        total = len(zipFile.namelist())
        updateProg = 1
        for file in zipFile.namelist():  # namelist is a list of every file in the zip
            updateProg += 1
            if (
                updateProg == 500
            ):  # only update meter every 500 files because there's 40k of them
                sg.one_line_progress_meter(
                    "Texture Extract",
                    zipFile.namelist().index(file),  # find current point in extraction
                    total,
                    "Extracting textures, please be patient",
                    no_button=True,
                )
                updateProg = 1
            zipFile.extract(file, "textures")
        sg.one_line_progress_meter(  # sometimes the bar doesn't get fully finished, this makes sure that happens
            "Texture Extract",
            total,
            total,
            "Extracting textures, please be patient",
            no_button=True,
        )
    os.remove("textures/textures.zip")
    sg.popup("Default textures have been downloaded.")


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
    if not os.path.exists(f"{folder}/pack.mcmeta"):  # see if we've already init'd
        sg.popup(
            "This folder isn't set up for a Resource Pack. Try using the 'New' option."
        )
        ControlledExit()
else:
    version = iSetup.InitSetup(
        folder
    )  # init setup returns a version field so we can copy the default ones
    sg.popup(
        f"Packutil will now copy the default texures for {version} to the project folder."
    )
    GUIFileCopy(f"textures/{version}/assets", f"{folder}/assets")
