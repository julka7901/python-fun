class PrzykładowaKlasa:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'w przykladowej klasie x to {self.x} a y to {self.y}'
    
przykład1 = PrzykładowaKlasa(4, 8)
print(str(przykład1))