from excel import Automate_excel
from directory_handling import Diretory_edit


class Menus:

    def __init__(self):
        print("Velkommen \n  Hva ønser du å gjøre?")
        print("For nytt prosjket skriv: new")
        print("For akonto: edit")
        print("For for å bytte: exit")
    
    def add_new_prodject(self):
        pass
    
    def edit_prodject(self):
        pass
        
    def change_prodject(self):
        pass
    
    def print_menu(self):
        print("For nytt prosjket skriv: new")
        print("For akonto: edit")
        print("For for å bytte: exit")
    

def main():
    
    action = input()
    
    if action == 'new':
        new_prodject = Automate_excel(action)
    
    

try:
    main()
except KeyboardInterrupt:
    print("Good bye . . . ")