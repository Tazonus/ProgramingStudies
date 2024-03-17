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

print("Zad:6")

class grid_calc:
    """Calculates in grid"""
    def __init__(self, equation = '235+72'):
        max = 0
        result = 0

        equation = equation.replace('-','$-')
        equation = equation.replace('+','$+')
        nums_str = equation.split('$')

        for x in nums_str:
            if('-' in x):
                x = x.removeprefix('-')
            elif('+' in x):
                x = x.removeprefix('+')
        
            if max < len(x):
                max = len(x)
        
            max +=1
            # to make gap between numbers and signs
        for x in nums_str:
            result += int(x)
            spaces = max - len(x)
            if('-' in x):
                
                x = x.replace('-','-' + self.make_space(spaces))
            elif('+' in x):
                x = x.replace('+','+' + self.make_space(spaces))
            else:
                x = self.make_space(spaces) + x
            print(x)

        result = str(result)
        print(self.make_space(max,'-'))
        print(self.make_space(max - len(result)-1), result)

    def make_space(self, howmany, ch = ' '):
        """Returns line of characters, if not specified returns spaces"""
        return ch * howmany



grid_calc()
        


