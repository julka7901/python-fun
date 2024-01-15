# Exercise Cats Everywhere
# Given the below class:

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def oldest(*args):
        return max(args)




# 1 Instantiate the Cat object with 3 cats.

# 2 Create a function that finds the oldest cat.

# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
        
Cat1 = Cat('lujek', 2)
Cat2 = Cat('enzo', 3)
Cat3 = Cat('pira', 10)

Oldest_cat = (Cat.oldest(Cat1.age, Cat2.age, Cat3.age))

print(f'najstaszy kot ma {Oldest_cat} lat')