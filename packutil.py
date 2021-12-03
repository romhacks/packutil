# packutil authored by team electronika
from tkinter import Button
import PySimpleGUI as sg
from os.path import exists

sg.theme("DarkPurple1")


def exit(reason=None):
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


event, values = sg.Window(
    "Welcome to packutil",
    [
        [sg.Text("Choose an existing project folder or make a new one.")],
        [sg.Button("Existing"), sg.Button("New")],
    ],
).read(close=True)


folder = sg.popup_get_folder("Choose a project folder")
if folder == None:
    exit("Folder choosing was cancelled.")

if event == "Existing":
    if not exists(f"{folder}/pack.mcmeta"):
        sg.popup(
            "This folder isn't set up for a Resource Pack. Try using the 'New' option."
        )
