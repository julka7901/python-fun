while True:
    try:
        age = int(input("podaj wiek: "))
        1/age
    except (ValueError, ZeroDivisionError) as err:
        print(f"ayo, to nie jest ppoprawny wiek!")
        continue
    else:
        print ('git')
        break


