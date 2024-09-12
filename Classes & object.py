"""# Defining Classes
class Dog:
    species = 'Canine'  # Class attribute

    def __init__(self, name, age):  # Constructor method
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
#Creating Objects
dog1 = Dog('Buddy', 3)
dog2 = Dog('Max', 5)

print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 5    """

"""
#Class Attributes and Methods
class Dog:
    species = 'Canine'  # Class attribute

    @classmethod
    def get_species(cls):  # Class method
        return cls.species

print(Dog.get_species())  # Output: Canine   """

"""#Instance Attributes and Methods
class Dog:
    species = 'Canine'

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def bark(self):  # Instance method
        return f'{self.name} is barking!'

dog1 = Dog('Buddy', 3)
print(dog1.bark())  # Output: Buddy is barking!    """


"""# Instance vs. Class Variables
class Dog:
    species = 'Canine'  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable

dog1 = Dog('Buddy', 3)
dog2 = Dog('Max', 5)

print(dog1.species)  # Output: Canine (shared)
print(dog2.name)     # Output: Max (unique)      """

"""#Method Overloading
class Math:
    def add(self, a, b=0):
        return a + b

m = Math()
print(m.add(5))  # Output: 5 (only one argument)
print(m.add(5, 10))  # Output: 15 (two arguments)   """

"""class Math:
    def add(self, *args):
        return sum(args)

m = Math()
print(m.add(5))          # Output: 5
print(m.add(5, 10))      # Output: 15
print(m.add(5, 10, 20))  # Output: 35      """


"""
#Static Methods
class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.multiply(5, 3))  # Output: 15    """

# Class Methods
class Dog:
    species = 'Canine'

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

dog1 = Dog('Buddy')
dog2 = Dog('Max')

print(dog1.species)  # Output: Canine
Dog.change_species('Feline')
print(dog2.species)  # Output: Feline
















