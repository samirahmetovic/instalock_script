import PySimpleGUI as sg
from instalock import instalock

# All the stuff inside your window.
layout = [
    [sg.Text('Agent selection: '), sg.Combo(values=['phoenix', 'reyna'], key='agent_selection', enable_events=True)]
]

# Create the Window
window = sg.Window('InstaLock', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'agent_selection':
        instalock(values['agent_selection'])

window.close()