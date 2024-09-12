"""#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

dog = Dog('Buddy')
print(dog.speak())  # Output: Buddy barks   """

"""#Overriding Methods
class Animal:
    def speak(self):
        return "Animal speaks."

class Dog(Animal):
    def speak(self):
        return "Dog barks."

dog = Dog()
print(dog.speak())  # Output: Dog barks   """

"""#Using super()
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the parent class's constructor
        self.breed = breed

    def speak(self):
        return super().speak() + f" The dog barks."

dog = Dog('Buddy', 'Golden Retriever')
print(dog.speak())  # Output: Buddy makes a sound. The dog barks.  """

"""#Multiple Inheritance
syntax:class Class1:
    pass

class Class2:
    pass

class ChildClass(Class1, Class2):
    pass

    """
"""#Multiple Inheritance
class Animal:
    def speak(self):
        return "Animal sound."

class Pet:
    def info(self):
        return "This is a pet."

class Dog(Animal, Pet):
    def speak(self):
        return "Dog barks."

dog = Dog()
print(dog.speak())  # Output: Dog barks
print(dog.info())   # Output: This is a pet     """

#Understanding Encapsulation
#Public: Accessible from anywhere.
#Protected (_var): Can be accessed within the class and subclasses.
#Private (__var): Accessible only within the class.


"""class Car:
    def __init__(self):
        self._fuel_level = 0  # Protected attribute

    def _refuel(self, amount):  # Protected method
        self._fuel_level += amount

class ElectricCar(Car):
    def charge(self):
        self._refuel(50)  # Accessing protected method from parent

car = ElectricCar()
car.charge()
print(car._fuel_level)  # Output: 50 (though it is protected, Python allows access)

"""

#Private Attributes:Private attributes or methods in Python are prefixed with __ (double underscores).
#They are not directly accessible outside the class, which enforces encapsulation.
"""class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Output: 100
# print(account.__balance)  # This would raise an AttributeError   """


#Property Decorators:Property decorators (@property) allow you to define methods that can be accessed like attributes.
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

circle = Circle(5)
print(circle.radius)  # Output: 5
circle.radius = 10
print(circle.radius)  # Output: 10
# circle.radius = -3  # This would raise a ValueError















































