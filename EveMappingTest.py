# import esipy
import os

def find_sys(iden):
    for i in range(len(systems)):
        if systems[i].id == iden:
            return i
    return

def clear():
    """_summary_
    """    
    os.system('cls' if os.name=='nt' else 'clear')

class System():    
    def __init__(self,iden, name, cl, mod):
        """_summary_

        Args:
            iden (_type_): _description_
            name (_type_): _description_
            cl (_type_): _description_
            mod (_type_): _description_
        """            
        self.id = iden
        self.name = name
        self.cl = cl
        self.mod = mod
        self.notes = []

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """               
        return self.name

class Wormhole:
    def __init__(self,iden, size, mass, syst):
        """_summary_

        Args:
            iden (_type_): _description_
            size (_type_): _description_
            mass (_type_): _description_
            syst (_type_): _description_
        """             
        self.id = iden
        self.size = size
        self.mass = mass
        self.syst = syst

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """               
        global systems
        s = [systems[find_sys(self.syst[0])], systems[find_sys(self.syst[1])]]
        return str(s[0]) + "-" + str(s[1])

def auth():
    """_summary_
    """    
    input("Sorry, work in progress.")

def add_system():
    """_summary_
    """    
    while True:
        name = input("Please, enter system name:\n")
        clear()
        while True:
            cl = input("Please, enter system class: (1-6)\n")
            clear()
            try:
                cl = int(cl)
            except Exception:
                continue
            if cl >= 1 and cl <= 6:
                break
        print("Please, enter system modificator:")
            

systems = []
wormholes = []
sys_num = 0
worm_num = 0
chara = 0

if __name__ == "__main__":
    while True:
        print("Welcome to EVE Online mapping tool.")
        print("Please, choice your action:")
        print("1. Authorise your character.")
        print("2. Add new system.")
        print("3. Add new wormhole.")
        print("4. Add new note about system.")
        print("5. Modify/Delete system.")
        print("6. Modify/Delete wormhole.")
        print("7. Build a route.")
        print("8. Exit")
        action = input()
        if action == "1":
            clear()
            auth()
        elif action == "2":
            clear()
            add_system()
        elif action == "3":
            pass
        elif action == "4":
            pass
        elif action == "5":
            pass
        elif action == "6":
            pass
        elif action == "7":
            input("Sorry, work in progress.")
        elif action == "8":
            action = input("Are you sure?(Y/N)")
            if action.lower() == "y" or action.lower() == "yes" or action.lower() == "1":
                exit()
        clear()
