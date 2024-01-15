some_list = ['a','b','c','d','e','b','f','n','n']

#1. przypisz wartosc do zmiennej, 2. sprawdz czy jest w liscie 3. wydrukuj jesli sie powtarza

duplikaty = []
for item in some_list:
    licz = some_list.count(item)
    if licz>1:
        if item not in duplikaty:
            duplikaty.append(item)
        
print(duplikaty)