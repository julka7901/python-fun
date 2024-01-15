def generator(num):
    for i in range(num):
        yield i

g = generator(10)

for item in generator(10):
    print(item+2)

next(g)
print(next(g))

