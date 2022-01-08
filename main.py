from excel import Automate_excel
from directory_handling import Diretory_edit


class Menus:

    def __init__(self):
        print("Velkommen \n  Hva ønser du å gjøre?")
        print("For nytt prosjket skriv: new")
        print("For akonto: edit")
        print("For for å bytte: exit")
    

    def add_new_prodject(self, action):
        
        new_prodject = Automate_excel(action)
        new_prodject.wb_save()

        
    def edit_prodject(self,action):
        edit_prodject = Automate_excel(action)


    def change_prodject(self):
        pass
    

    def print_menu(self):
        print("For nytt prosjket skriv: new")
        print("For akonto: edit")
        print("For for å bytte: exit")
    

def main():
    while 1:
        menu = Menus()
        action = input()
    
        if action == 'new':
            menu.add_new_prodject(action)

        if action == 'edit':
            menu.edit_prodject(action)
     

try:
    main()
except KeyboardInterrupt:
    print("Good bye . . . ")