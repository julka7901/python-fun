class User:
    def sign_in(self):
        print("logged in")
    
    def __init__(self, email):
        self.email = email

class Wizard (User):
    def __init__(self, name, power):
       
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} użyłes mocy {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows (self):
        print(f'{self.name} pozostało {self.num_arrows} strzał')

class Hybryda (Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)
    

wizard1 = Wizard ('Merlin', 'freeze')
archer1 = Archer ('Robin', 20)

hybryda1 = Hybryda("Borg", "MOC", 50)

print(hybryda1.sign_in())