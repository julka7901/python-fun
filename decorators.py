def dekorator(func):
    def wrap_funct(*args, **kwargs):
        print("*******")
        func(*args, **kwargs)
        print("*******")
    return wrap_funct

@dekorator #dodaj przed zdefiniowaną funkcją aby dołączyć do funkcji
def hello(greeting, emoji):
    print(greeting, emoji)


hello("hejka", ":]")