import random


#Zad 1:
def gen_pass(length = 8):
    printable_ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    #from https://stackoverflow.com/questions/2444447/string-that-contains-all-ascii-characters

    temp_pass = ''
    for i in range(length):
        temp_pass += random.choice(printable_ASCII)
    return temp_pass

print(gen_pass())
print(gen_pass())
print(gen_pass())

#Zad 2,5:

#Zad 3:

#Zad 4:

#Zad 6:

#need to change that shitty name later
class grid_calc:
    def __init__(self, equation ='1+2-3'):
        equation =equation.replace('-','+-')
        print(equation)
        self.equation_List = equation.split('+')
        print(self.equation_List)




grid_calc()
        


