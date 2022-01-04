import shutil
import os


class Diretory_edit:

    def __init__(self, path):
        self.path = path

    def create_dir(self, dir_name):
        os.makedirs(name=dir_name)




if __name__ == "__main__":
    cdir = Diretory_edit

    cdir.create_dir('My dir 123')
