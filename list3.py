import re
brackets_open  = "{[(<"
brackets_close = "}])>"

#removing all symbols except brackets
input = input("Write equation you want to check: \n")
tempvector = []
for x in input:
    if x in brackets_open:
        tempvector.append(x)
    elif x in brackets_close:
        id = brackets_close.index(x)
        if tempvector[-1] == brackets_open[id]:
            tempvector.pop()
        else:
            print("expresion is invalid")#it was
            break
if tempvector == []:
    print("expresion is valid")
