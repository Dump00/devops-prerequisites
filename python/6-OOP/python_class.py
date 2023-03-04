class Student:
    name = ''
    age = 0


student_one = Student()
student_one.name = 'Luffy'
student_one.age = 16

print(student_one.age, student_one.name)


# Inheritance

class Animal:
    def eat(self):
        print('I can eat!')
    def sleep(self):
        print('I can sleep!')

# derived class
class Dog(Animal):
    def bark(self):
        print('I can bark')


dog = Dog()

dog.bark()
dog.eat()
dog.sleep()


# Encapsulation

class Computer:

    # constructor function
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()