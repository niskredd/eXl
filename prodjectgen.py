import datetime
import PySimpleGUI as sg
import pandas as pd
from excel import Automate_excel


sg.theme('DarkTeal9')

PRO_FILE = 'C:\\Users\\NilsAndreasSkreddern\\Frøiland Bygg Skade AS\\FBS Fellesområde - 833 Nils Andreas Skreddernes\\833 Nils Andreas Skreddernes Prosjektliste 2022.xlsx'
PRO_FILE_CPP = 'C:\\Users\\NilsAndreasSkreddern\\Frøiland Bygg Skade AS\\FBS Fellesområde - 833 Nils Andreas Skreddernes\\833 Nils Andreas Skreddernes Prosjektliste 2022 copy.xlsx'
FOLDER_DIR = 'C:\\Users\\NilsAndreasSkreddern\\Frøiland Bygg Skade AS\\FBS Fellesområde - 833 Nils Andreas Skreddernes'

df = pd.read_excel(PRO_FILE, sheet_name=0, skiprows=14)

layout = [
    [sg.Text('Fyll inn info:  ')],
    [sg.Text('Dato:         ', size=(15,1)), sg.InputText(key='Dato')],
    [sg.Text('Addresse:     ', size=(15,1)), sg.InputText(key='Arbeidssted/Prosjekt')],
    [sg.Text('Postnummer:   ', size=(15,1)), sg.InputText(key='Postnummer')],
    [sg.Text('Poststed:     ', size=(15,1)), sg.InputText(key='Poststed')],
    [sg.Text('Type:         ', size=(15,1)), sg.Combo(['Fakturerbar', 'Reklamasjon'], key='Type')],
    [sg.Text('Skadeårsak:   ', size=(15,1)), sg.Combo(['Vann', 'Brann', 'Innbo/løsøre', 'Annet', 'Skadedyr', 'Frost'], key='Skadeårsak')],
    [sg.Text('Info:         ', size=(15,1)), sg.InputText(key='Info:')],
    [sg.Text('Selskap:      ', size=(15,1)), sg.Combo(['IF Skadeforsikring', 'Gjensidige', 'Tryg', 'KLP', 'Knif', 'Landkreditt'], key='Selskap')],
    [sg.Text('Skadenummer:  ', size=(15,1)), sg.InputText(key='skadenummer')],
    [sg.Text('Kunde:        ', size=(15,1)), sg.InputText(key='Navn på kunde')],
    [sg.Text('Sakbehandler: ', size=(15,1)), sg.InputText(key='S_beh')],
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
        sbh = values['S_beh']
        values.pop('S_beh')
    
        #for row in range(15, 30):
        print(df.at[15, 'Dato'])
        #df = df.append(values, ignore_index=True)
        #df.to_excel(PRO_FILE_CPP, index=False)
        
        
        #pws = Automate_excel('new', p_nr, values['Arbeidssted/Prosjekt'])
        #pws.fillin_sheet()
        #sg.popup('Perosjekt opprettet')
   
        
window.close()