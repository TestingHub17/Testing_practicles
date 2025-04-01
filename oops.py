# class is blueprint of objects, Objects have attributes(name, age, color) and behavior(dancing, singing)
# Why need to use OOPS -  Structuring programs so that properties and behavior bundled in Objects
# Encapsulation, Inheritance, Abstraction, and Polymorphism.



# ---------------------------- ABSTRACTION --------------------------------

# Hiding the details is called data abstraction
# Abstract class is a class in which one or more abstract methods are defined.
# When a method is declared inside the class without its implementation is known as abstract method.
# Concrete Method : Method in abstract class which already have the implementation

"""from abc import ABC, abstractmethod

class Bird(ABC):

    @abstractmethod
    def dancing(self):
        pass

    def check(self):
        pass

class child(Bird):

    def __init__(self, age):
        self.age = age

obj = child(15)
print(obj)"""






# ---------------------------- POLYMORPHISM -----------------------------------

# Polymorphism is a foundational concept in programming that allows entities like functions, methods or operators
# to behave differently based on the type of data they are handling.
# 1 - Compile time Polymorphism : Method overloading
#  2 - Runtime Polymorphism : Method Overriding - Runtime decide on basis of type of data method get to perform task

# Python program to demonstrate
# Defining parent class
"""class Parent:

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)

    def check(self):
        print("Check it")

    # Defining child class


class Child(Parent):

    # Constructor
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)
        print(f"super call ")
        print(super().show())
        print(Parent().show())

    # Driver's code


# obj1 = Parent()
obj2 = Child()

# obj1.show()  # Should print "Inside Parent"
obj2.show()  # Should print "Inside Child"""

"""def add(a, b):
    return a+b

def add(a, b, c=0):
    return a+b*c

add(1,2)
print(add("hello ", "World"))
print(add([1,2], [2,3]))

from multipledispatch import dispatch

# passing one parameter


@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

# passing two parameters


@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

# you can also pass data type of any value as per requirement


@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with 2 arguments
product(2, 3)  # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2)  # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997
"""





# -------------------------- ENCAPSULATION ---------------------------------------

# Encapsulation is the process of hiding the internal state of an object and requiring all interactions to be performed through an object’s methods
# Python achieves encapsulation through public, protected and private attributes.

# PROTECTED MEMBERS : Protected members are identified with a single underscore (_).
# They are meant to be accessed only within the class or its subclasses.

"""class Parent:

    def __init__(self):
        self.__age = 20



class Child(Parent):

    def __init__(self):
        super().__init__()
        # self.age = 30
        self.name = "Rachana"

    def display(self):
        print(self.__age)
        print(self.name)

obj = Child()
obj._age = "Diya"
obj.display()"""












# -------------------------------------- INHERITANCE ---------------------------------

# Single Inheritance: A child class inherits from one parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A class is derived from a class which is also derived from another class.
# Hierarchical Inheritance: Multiple classes inherit from a single parent class.
# Hybrid Inheritance: A combination of more than one type of inheritance.


# Multiple Inheritance

"""class Parent1:

    def __init__(self):
        self.language = ['English']
        self.country = 'America'
        print(f'The Parent1 Language is {self.language} and country {self.country}')

    # def __str__(self):
    #     return f'The Parent1 Language is {self.language} and country {self.country}'

class Parent2:

    def __init__(self):
        self.language = ['Hindi']
        self.country = 'India'
        print(f'The Parent2 is {self.language} and country {self.country}')

    # def __str__(self):
    #     return f'The Parent2 is {self.language} and country {self.country}'

class Child(Parent1, Parent2):

    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)


obj = Child()
print(obj)"""


# Hierarchical Inheritance
"""class Parent:
    data = [1]

    def __init__(self):
        self.language = ['English']
        data = [1]

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.language.append('Hindi')
        self.data.append(2)

class Child2(Parent):

    def __init__(self):
        super().__init__()
        self.language.append('Gujarati')
        super().data.append(3)



obj_p = Parent()

print(obj_p.data)
print(obj_p.language)
Obj = Child()
obj_c = Child2()
print(Obj.data)
print(Obj.language)
print(obj_c.data)
print(obj_c.language)

if isinstance(obj_c, Child):
    print(True)"""

















"""class Dog:

    # class attribute only make difference if updated using class name
    count = 0

    # dunder method which have __ in front
    def __init__(self, name, age):
        # instance attributes - Created in this method call instance attributes
        self.name = name
        self.age = age

    # print object then this method executed by default
    def __str__(self):
        return f'The dog name is {self.name} with age {self.age}'"""



