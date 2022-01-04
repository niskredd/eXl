from openpyxl import Workbook


workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename="hello_world.xlsx")


class excel_workbook:

    def __init__(self, path, file):
        self.path = path
        self.file = file

    def write_to_sheet(self, sheet, data_dir):

        

        for data in len(data_dir):
            

