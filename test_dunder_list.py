class MojaLista(list):
    def __init__ (self, *args):
        super().__init__(*args)
        self.suma = sum(self)


moja_lista = MojaLista([1,2,3,4])
print(moja_lista.suma)

txt = "Hello World"

print(bool("abc"))