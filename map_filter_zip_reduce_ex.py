from functools import reduce


def WielkieLitery (item):
    return item.capitalize()
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

print (list(map(WielkieLitery, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

def Over50 (item):
    return item>50

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(Over50, scores)))


def accumulator(acc,item):
    
    return acc + item
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(accumulator, scores+my_numbers))

print(reduce(lambda acc, item:acc + item, scores+my_numbers)) #lambda - jednorazowa funkcja
