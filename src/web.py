import PySimpleGUI as sg
import requests


def GUIDownloadFile(url, dst): #download texture file from server and make a GUI progress dialog
    response = requests.get(url, stream=True)
    byteSize = int(response.headers.get("content-length", 0))
    bs = 1048576
    progressIterator = 0
    with open(dst, "wb") as file:
        for data in response.iter_content(bs): #runs for each chunk of data defined in bs
            progressIterator = progressIterator + len(data)
            sg.one_line_progress_meter(
                "Texture Download",
                progressIterator,
                byteSize,
                "Downloading textures, please be patient",
                no_button=True,
            )
            file.write(data)
