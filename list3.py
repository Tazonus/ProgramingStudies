import re
import sys

#task 5
def main():
    brackets_open  = "{[(<"
    brackets_close = "}])>"

    input = sys.argv[1]
    tempvector = []
    isvalid = True
    for x in input:
        if x in brackets_open:
            tempvector.append(x)
        elif x in brackets_close:
            id = brackets_close.index(x)
            if len(tempvector) == 0:
                isvalid = False
                break
            if tempvector[-1] == brackets_open[id]:
                tempvector.pop()
            else:
                isvalid = False
                break
    if isvalid and tempvector == []:
        print("expresion is valid")
    else:
        print("expresion is invalid")

if __name__ == "__main__":
    main()