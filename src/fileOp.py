import os
import shutil
import PySimpleGUI as sg


def countFiles(dir):
    files = []

    if os.path.isdir(dir):
        for path, dirs, filenames in os.walk(dir):
            files.extend(filenames)

    return len(files)


def makedirs(dest):
    if not os.path.exists(dest):
        os.makedirs(dest)


def GUIFileCopy(src, dest):
    numFiles = countFiles(src)
    if numFiles > 0:
        makedirs(dest)
        fileIterator = 1
        numCopied = 0
        for path, dirs, filenames in os.walk(src):
            for directory in dirs:
                destDir = path.replace(src, dest)
                makedirs(os.path.join(destDir, directory))
        for path, dirs, filenames in os.walk(src):
            for sfile in filenames:
                srcFile = os.path.join(path, sfile)

                destFile = os.path.join(path.replace(src, dest), sfile)

                shutil.copy(srcFile, destFile)

                numCopied += 1
                fileIterator += 1
                if fileIterator == 500:
                    sg.one_line_progress_meter(
                        "File Copy",
                        numCopied,
                        numFiles,
                        "Copying files, please be patient",
                        no_button=True,
                    )
                    fileIterator = 1
        sg.one_line_progress_meter(
            "File Copy",
            numFiles,
            numFiles,
            "Copying files, please be patient",
            no_button=True,
        )
