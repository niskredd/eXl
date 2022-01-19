import pandas as pd
from datetime import date
from openpyxl import workbook, load_workbook


pathg = "C:\\Users\\Nils\\OneDrive\\Documents\\Programering\\Python\\Excel 2\\eXl"
fileg = "833 Nils Andreas Skreddernes Prosjektliste 2022.xlsx"
copy_file = "test_file.xlsx"



class Prosject_list():
    
    def __init__(self, path, file):
        self.path = path
        self.filet = file
        self.file = pd.read_excel(path + '\\' + file)
        
        key1 = self.file.keys()
        self.df = pd.DataFrame(self.file, index=range(14,513), columns=key1)
        
    
    def check_free_row(self):
        for num in range(14,513):
            if self.df.loc[num].isnull().values.any():
                return num
            else:
                return 666
    
    
    def add_prodject(self, dict_info):
        dfr = self.df.iloc[self.check_free_row()-10]
        dfr.columns = self.df.keys()
        dict_info.update({'Dato': str(date.today())})
        dfr[0] = date.today()
        dict_info.update({'Prosjektnummer': str(dfr[1])})
        dfr[2] = dict_info['Arbeidssted/Prosjekt']
        dfr[3] = dict_info['Postnummer']
        dfr[4] = dict_info['Poststed']
        dfr[5] = dict_info['Type']
        dfr[6] = dict_info['Skadeårsak']
        dfr[7] = dict_info['Info']
        dfr[8] = dict_info['Selskap' ]
        dfr[9] = dict_info['skadenummer']
        dfr[10] = dict_info['Navn på kunde' ]

        print(pd)
        return dict_info
    
    
    def print_file(self):
        print(self.file)
        print(self.df)
   

    def save_wb(self):
        pass
        



if __name__ == "__main__":
    prod_dict = {
        'Arbeidssted/Prosjekt'  : 'Skogen 2',
        'Postnummer'            : '2211',
        'Poststed'              : 'Bloksberg',
        'Selskap'               : 'Tryg',
        'Type'                  : 'Fakturerbar',
        'skadenummer'           : '1324567',
        'Navn på kunde'         : 'Knut',
        'Skadeårsak'            : 'Vann',
        'Prosjektnummer'        : '',
        'Info'                  : "Rørbrudd",
        'Dato'                  : ''
    }
    
    
    
    pl = Prosject_list(pathg, fileg)
    print(pl.add_prodject(prod_dict))
    
    pl.save_wb()