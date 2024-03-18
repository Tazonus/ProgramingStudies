import random
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

#Zad 1:
def gen_pass(length = 8):
    printable_ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    #from https://stackoverflow.com/questions/2444447/string-that-contains-all-ascii-characters

    temp_pass = ''
    for i in range(length):
        temp_pass += random.choice(printable_ASCII)
    return temp_pass

#Zad 2,5:

class Watermarker:
    def __init__(self, imagePath, watermarkPath, set_size, name):
        im = Image.open(imagePath)
        watermark = Image.open(watermarkPath)

        im = im.resize(set_size).convert('RGBA')
        watermark = watermark.resize([im.width//2, im.height//2]).convert('RGBA')
        watermark_data = watermark.getdata()
        watermark_data = [(r, g, b, (a*3)//4) for r, g, b, a in watermark_data]
        watermark.putdata(watermark_data)
        
        canvas = Image.new('RGBA', set_size, (0, 0, 0, 0))
        canvas.paste(watermark, (0, 0), mask=watermark,)
        final_image = Image.alpha_composite(im.convert('RGBA'), canvas)
        final_image.show()
        
#Zad 3:

#Zad 4:

#Zad 6:

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


if __name__ == '__main__':
    print("Zad:1")
    print('Generated password:',gen_pass())
 
    path1 = "image1.jpg"
    path2 = "/home/tazos/Documents/pwr/Programowanie/image2.jpg"
    Watermarker(path1, path2, [440,880], 'testname')


    print("Zad:6")
    grid_calc()