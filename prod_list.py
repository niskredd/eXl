from operator import index
import pandas as pd

pathg = "C:\\Users\\Nils\\OneDrive\\Documents\\Programering\\Python\\Excel 2\\eXl"
fileg = "833 Nils Andreas Skreddernes Prosjektliste 2022.xlsx"
copy_file = "test_file.xlsx"



class Prosject_list():
    
    def __init__(self, path, file):
        self.path = path
        self.filet = file
        self.file = pd.read_excel(path + '\\' + file)

    def save_wb(self):
        self.wb.save(self.path + copy_file)        
    
    def check_free_row(self):
        df = pd.DataFrame(self.file, index=range(14,314))
        print(df.keys())
        for num in range(300):
            print(df.lookup(num, 0))
            print(df.loc[num].at['Unnamed: 0'])



if __name__ == "__main__":
    pl = Prosject_list(pathg, fileg)
    print(pl.check_free_row())