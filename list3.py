import re
import sys

#task 5

brackets_open  = "{[(<"
brackets_close = "}])>"

#removing all symbols except brackets
input = str(sys.argv)
tempvector = []
for x in input:
    if x in brackets_open:
        tempvector.append(x)
    elif x in brackets_close:
        id = brackets_close.index(x)
        if len(tempvector) == 0:
            print("expresion is invalid")
            break
        if tempvector[-1] == brackets_open[id]:
            tempvector.pop()
        else:
            print("expresion is invalid")#it was
            break
if tempvector == []:
    print("expresion is valid")
else:
    print("expresion is invalid")