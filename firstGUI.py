picture = [
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

pełne = "*"
puste = " "

i = 0
while i<5:

    for row in picture:
        for pixel in row:
            if pixel:
                print(pełne,end= ' ')
                #end = " " -nie przeskakuje do kolejnej linijki 
                #(tak jak jest standardowo) tylko daje spacje
            else:
                print(puste, end= ' ')
        print() #przechodzi do kolejnej linijki, 
                #bez tego wszystko jest w jednej linii
    i=i+1