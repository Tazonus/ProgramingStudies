import random
import math

class Vector:
    #konstruktor z możliwością ustawienia wielkości, automatycznie wypełnia wartości 0
    def __init__(self, size = 3):
        if(size < 1):
            print("Cannot make a vector : (")
            return 0
        
        self.size = size
        self.vector = []

        for i in range(size):
            self.vector.append(0)

    #Dobiera wektorowi losowe liczby z zakresu [-max,max], domyślnie max = 10
    def randomize(self, max = 10):
        for i in range(self.size):
            self.vector[i] = random.uniform(-max,max)

    #ładuje wektor z listy
    def load(self, lista = {0,0,0}):
        self.vector = []
        self.size = len(lista)
        for i in range(self.size):
            self.vector.append(lista[i])

    #operator dodawania
    #nie wyrzuca VallueError ale wychodzi na jedno bo wyskakuje przy różnych rozmiarach
    def __add__(self, other):
        try:
            temp_vector = Vector(self.size)
            for i in range(self.size):
                temp_vector[i] = self.vector[i] + other.vector[i]
            return temp_vector
        except ValueError:
            print("VallueError, róznej wielkości wektory")
        except IndexError:
            print("IndexError choć miał być VallueError, na jedno wychodzi, nie można przeprowadzić operacji przez róznej wielkości wektory")            
        
    #operator odejmowania
    #to samo co powyżej w kwesti VallueError
    def __sub__(self,other):
        try:
            temp_vector = Vector(self.size)
            for i in range(self.size):
                temp_vector[i] = self.vector[i] - other.vector[i]
            return temp_vector
        except ValueError:
            print("VallueError, róznej wielkości wektory")
        except IndexError:
            print("IndexError choć miał być VallueError, na jedno wychodzi, nie można przeprowadzić operacji przez róznej wielkości wektory")    
    
    #operator mnożenia używany do
    #a) mnożenia przez skalar
    #b) iloczynu skalarnego
    #sprawdza czy to z czym się mnoży(other) jest floatem, jak wyłapie error to znaczy że nie i próbuje od razu przejść do mnożenia z drugim wektorem
    def __mul__(self, other):
        isfloat = True
        try:
            float(other)
        except TypeError:
            isfloat = False

        if(isfloat):    
            temp_vector = []
            for i in range(self.size):
                temp_vector.append(other * self.vector[i])
            return temp_vector
        elif(self.size == other.size):
            skalar = 0
            for i in range(self.size):
                skalar += self.vector[i] * other.vector[i]
            return skalar
            
    #zwraca długość wektora    
    def length(self):
        len = 0
        for i in range(self.size):
            len += pow(self.vector[i],2)
        return math.sqrt(len)
    
    #zwraca sume elementów wektora
    def sum(self):
        sum = 0
        for i in range(self.size):
            sum += self.vector[i]
        return sum
    
    #Daniel
    def print(self):
        print(self.vector)
    
    #The Cooler Daniel
    def __str__(self):
        return f"{self.vector}"
    
    #operator [] służacy do podejrzenia wartości  - Getter
    def __getitem__(self, key):
        return self.vector[key]
    #operator [] służący do przypisania wartości  - Setter
    def __setitem__(self, key, value):
        self.vector[key] = value

    #operator in sprawdzający przynależność elementu do wektora.
    def __contains__(self, item):
        return item in self.vector


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