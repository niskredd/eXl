import datetime
import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkTeal9')

PRO_FILE = ''
FOLDER_DIR = ''

df = pd.read_excel(PRO_FILE)

layout = [
    [sg.Text('Fyll inn info:  ')],
    [sg.Text('Addresse:', size=(15,1)), sg.InputText(key='Address')],
    [sg.Text('Beboer:', size=(15,1)), sg.InputText(key='Beboer')],
    [sg.Text('Skadenummer:', size=(15,1)), sg.InputText(key='S_num')],
    [sg.Text('Sakbehandler:', size=(15,1)), sg.InputText(key='S_beh')],
    [sg.Text('Selskap:', size=(15,1)), sg.Combo(['IF Skadeforsikring', 'Gjensidige', 'Tryg', 'KLP', 'Knif', 'Landkreditt'], key='Forsikring')],
    [sg.Text('Skadetype:', size=(15,1)), sg.Combo(['Vann', 'Brann', 'Innbo', 'Annet', 'Skadedyr', 'Frost'], key='Type')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Nytt Prosjekt', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        print(event, values)
        
window.close()