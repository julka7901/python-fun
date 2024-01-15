username = input("podaj nick: ")
haslo = input("podaj hasło: ")
ukryj_haslo = "*" * len(haslo)

print(f"hej {username}, twoje haslo {ukryj_haslo} ma {len(haslo)} znakow")