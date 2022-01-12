import datetime
import PySimpleGUI as sg
import pandas as pd
from excel import Automate_excel


sg.theme('DarkTeal9')

PRO_FILE = ''
FOLDER_DIR = ''

df = pd.read_excel(PRO_FILE)

layout = [
    [sg.Text('Fyll inn info:  ')],
    [sg.Text('Dato:', size=(15,1)), sg.InputText(key='Dato')],
    [sg.Text('Addresse:', size=(15,1)), sg.InputText(key='Addresse')],
    [sg.Text('Kunde:', size=(15,1)), sg.InputText(key='Kunde')],
    [sg.Text('Skadenummer:', size=(15,1)), sg.InputText(key='S_num')],
    [sg.Text('Sakbehandler:', size=(15,1)), sg.InputText(key='S_beh')],
    [sg.Text('Selskap:', size=(15,1)), sg.Combo(['IF Skadeforsikring', 'Gjensidige', 'Tryg', 'KLP', 'Knif', 'Landkreditt'], key='Forsikring')],
    [sg.Text('Skadetype:', size=(15,1)), sg.Combo(['Vann', 'Brann', 'Innbo', 'Annet', 'Skadedyr', 'Frost'], key='Type')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Nytt Prosjekt', layout)


def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        print(event, values)
    """ df = df.append(values, incnore_index=True)
        df.to_excel(PRO_FILE, index=False)
        sg.popup('Perosjekt opprettet')
    """
        
window.close()