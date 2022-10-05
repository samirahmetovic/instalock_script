import PySimpleGUI as sg
from instalock import instalock
from get_agents import get_agent_list
import threading

agents = get_agent_list()

# All the stuff inside your window.
layout = [
    [sg.Text('Agent selection: '), sg.Combo(values=agents, key='agent_selection', enable_events=False)],
    [sg.Button("start", key="start"), sg.Text(key="status")],
    [sg.Text("__________________________________")],
    [sg.Text("Advanced:")],
    [sg.Text("scaling"), sg.Input("1.0", size=(5, 5))]
]

# Create the Window
window = sg.Window('InstaLock', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'start':
        x = threading.Thread(target=instalock, args=(values['agent_selection'], "en", window["status"]))
        x.start()
        window["status"].update("waiting for Agent select...")

        # instalock(values['agent_selection'], "en")

window.close()
