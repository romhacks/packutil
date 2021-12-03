import PySimpleGUI as sg

sg.theme("DarkPurple1")


def InitSetup(folder):
    versionMap = {
        "1.6.1 - 1.8.9": 1,
        "1.9 - 1.10.2": 2,
        "1.11 - 1.12.2": 3,
        "1.13 - 1.14.4": 4,
        "1.15 - 1.16.1": 5,
        "1.16.2 - 1.16.5": 6,
        "1.17.x": 7,
        "1.18.x": 8,
    }

    event, values = sg.Window(
        "Resource Pack Initialization",
        [
            [
                sg.Text(
                    "Here you will fill out the information regarding the Resource Pack."
                )
            ],
            [
                sg.Text("Pack Description"),
                sg.Input(),
            ],
            [
                sg.Text("Minecraft version"),
                sg.Combo(
                    [
                        "1.6.1 - 1.8.9",
                        "1.9 - 1.10.2",
                        "1.11 - 1.12.2",
                        "1.13 - 1.14.4",
                        "1.15 - 1.16.1",
                        "1.16.2 - 1.16.5",
                        "1.17.x",
                        "1.18.x",
                    ]
                ),
            ],
            [sg.Button("Submit")],
        ],
    ).read(close=True)
    mcVersion = versionMap[values[1]]
    description = values[0]
    packFile = open(f"{folder}/pack.mcmeta", "w")
    packFile.write(f"""
{{
  "pack": {{
    "pack_format": {mcVersion},
    "description": "{description}"
  }}
}}
    """)
    packFile.close()