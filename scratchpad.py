# this is literally just stuff I want to remember it doesn't do anything lmao
import PySimpleGUI as sg

# sg.theme("DarkPurple1")  # Add a touch of color

# window = sg.Window('Enter a number', [[sg.Text("Pick number")], [sg.Input()], [sg.Ok()]])

# event, values = window.read()

# window.close()

# sg.Popup(event, values)

layout = [
    [sg.Text("Persistent window")],
    [sg.Input()],
    [sg.Input()],
    [sg.Button("Read"), sg.Exit()],
]

window = sg.Window("Window that stays open", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    print(event, values)

window.close()
