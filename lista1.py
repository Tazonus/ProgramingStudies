import random
import math

class Vector:
    """
    A class representing a vector.

    Attributes:
        size (int):     size of a vector
        values(list):   holds values for vector
        
    """
    def __init__(self, size = 3):
        """
        Initializes a Vector object.

        Parameters:
            size (int): size of a vector
        """
        if(size < 1):
            print("Cannot make a vector :(")
            return 0
        
        self.size = size
        self.values = []

        for i in range(size):
            self.values.append(0)

    def randomize(self, max = 10):
        """
        Randomizes Vector values in range

        Parameters:
            max (float):    defines max range [-max,max]
        """
        for i in range(self.size):
            self.values[i] = random.uniform(-max,max)

    def load(self, input):
        '''Loads vector from list'''
        self.values = []
        self.size = len(input)
        for i in range(self.size):
            self.values.append(input[i])
    
    def __add__(self, other):
        '''Adding operator'''
        try:
            temp_vector = Vector(self.size)
            for i in range(self.size):
                temp_vector[i] = self.values[i] + other.values[i]
            return temp_vector
        except ValueError:
            print("VallueError, Different size vector")
        except IndexError:
            print("IndexError, Different size vector")                   

    def __sub__(self,other):
        '''subtract operator'''
        try:
            temp_vector = Vector(self.size)
            for i in range(self.size):
                temp_vector[i] = self.values[i] - other.values[i]
            return temp_vector
        except ValueError:
            print("VallueError, Different size vector")
        except IndexError:
            print("IndexError, Different size vector")    
    
    def __mul__(self, other):
        '''Multiplying operator used to multiply by scalar or dot product'''

        if(isinstance(other,(float,int))):    
            temp_vector = []
            for i in range(self.size):
                temp_vector.append(other * self.values[i])
            return temp_vector
        
        elif(isinstance(other,Vector)):
            try:
                scalar = 0
                for i in range(self.size):
                    scalar += self.values[i] * other.values[i]
                return scalar
            except ValueError:
                print("VallueError, Different size vector")
            except IndexError:
                print("IndexError, Different size vector")  
            
    def length(self):
        '''Returns length of vector'''
        len = 0
        for i in range(self.size):
            len += pow(self.values[i],2)
        return math.sqrt(len)
    
    def sum(self):
        '''Returns Sum of Vector values'''
        sum = 0
        for i in range(self.size):
            sum += self.values[i]
        return sum
    
    #Daniel
    def print(self):
        '''prints all values, but you can also use print(YourVector)'''
        print(self.values)
    
    #The Cooler Daniel
    def __str__(self):
        '''Returns vector as a string'''
        return f"{self.values}"
    
    def __getitem__(self, key):
        '''[] operator getter'''
        return self.values[key]
    
    def __setitem__(self, key, value):
        '''[] operator setter'''
        self.values[key] = value

    def __contains__(self, item):
        '''in operator'''
        return item in self.values

if __name__ == '__main__':
    myVector = Vector()
    myVector.randomize()
    myVector.print()
    myVector.load([1,2,2])
    myVector.print()
    print(myVector.length())
    print(myVector.sum())
    print(myVector * 2)
    print(myVector * myVector)
    print(myVector[0])
    print(myVector)
    print(myVector+myVector)
    print(myVector-myVector)
    mySecondVector = Vector(4)
    print(mySecondVector + myVector)
    print(mySecondVector - myVector)
    print(1 in myVector)
    print(7 in myVector)
    myVector[0] = 123
    print(myVector)