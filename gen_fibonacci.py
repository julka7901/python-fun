
def Fib (index):
    obecny, kolejny = 0,1
    for i in range (index):
        yield obecny
        chwilowy = obecny
        obecny, kolejny = kolejny, obecny + kolejny
        

for x in Fib(10):
    print(x)
