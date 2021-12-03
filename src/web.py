import PySimpleGUI as sg
import requests


def GUIDownloadFile(url, dst):
    response = requests.get(url, stream=True)
    byteSize = int(response.headers.get("content-length", 0))
    bs = 1048576
    progressIterator = 0
    with open(dst, "wb") as file:
        for data in response.iter_content(bs):
            progressIterator = progressIterator + len(data)
            sg.one_line_progress_meter(
                "Texture Download",
                progressIterator,
                byteSize,
                "Downloading textures, please be patient",
                no_button=True,
            )
            file.write(data)
