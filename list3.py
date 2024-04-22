import re
brackets_open = "{[(<"
brackets_close = ">)]}"

#removing all symbols except brackets
input = input("Write equation you want to check: \n")
tempvector = []
for x in input:
    if x in brackets_open:
        tempvector.append(x)
    elif x in brackets_close:
        if tempvector[-1] == x:
            tempvector.pop
if tempvector == []:
    print("expresion is valid")
else:
    print('expresion is invalid')#or my code is bad