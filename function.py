#highest_even number
def highest_even(li):
    parzyste = []
    for item in li:
        if item %2==0:
            parzyste.append(item)
    return max(parzyste)


print (highest_even([11,1,2,3,4,8,5,10]))