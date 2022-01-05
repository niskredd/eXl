import shutil
import os


class Diretory_edit:

    def __init__(self):
        self.path = "C:\\Users\\NilsAndreasSkreddern\\Frøiland Bygg Skade AS\\FBS Fellesområde - 833 Nils Andreas Skreddernes"

    def create_dir(self, dir_name):
        os.makedirs(name=dir_name)
     
    def set_dir(self, dir_name):
        path = os.getcwd()
        if not os.path.exists(path+"\\"+dir_name):
            self.create_dir(dir_name)
        
        return path + "\\" + dir_name
        
    def content(self):
        for dir in os.listdir():
            print(dir + '\n')
    
    def change_dir(self, path):
        os.chdir(path)
        
    def starts_with_dir(self, searching):
    
        for directs in os.listdir(os.getcwd()):
            if directs.startswith(searching):
                print("Funnet")
                return directs
                break
        
        print("Finner ikke mappe som starter med:  " + searching)
    
    
    
 




if __name__ == "__main__":
    cdir = Diretory_edit()

    cdir.set_dir('Test')
    cdir.starts_with_dir('Test')
    
