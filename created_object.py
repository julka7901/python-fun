class PlayerCharacter:
    membership = True #class object attribute - not dynamic, can't modify
    def __init__(self, name = 'anonim', age = 0):
        if age>1:
            self._name = name #attributes
            self._age = age

    def shout(self): #method
        print(f'my ame is {self.name}')    
        return "done" #inaczej oddaje none
    
    @classmethod #zmiana atrybutów
    def adding_things(cls,num1,num2):
        return cls('Teddy', num1 + num2)
    
    @classmethod #tutaj nie zmienimy atrybutów
    def adding_things2(num3, num4):
        return num3 + num4

    def speak(self):
        print(f'mam na imie {self.name} mam {self.age} lat')
#player1 = PlayerCharacter("cindy",23)
    

player2 = PlayerCharacter.adding_things(2,3)

player2.speak()
#Private atribute - cos czego nie chcemy zeby ktokolwiek zmienial bedzie mialo podłogę przed nazwą np. _name
