# class Parrot:

#     # class attribute
#     name = ""
#     age = 0


# # create parrot1 object
# parrot1 = Parrot()
# parrot1.name = "Blu"
# parrot1.age = 10

# # create another object parrot2
# parrot2 = Parrot()
# parrot2.name = "Woo"
# parrot2.age = 15

# # access attributes
# print(f"{parrot1.name} is {parrot1.age} years old")
# print(f"{parrot2.name} is {parrot2.age} years old")


# # base class
# class Animal:

#     name = ""

#     def eat(self):
#         print("I can eat!")

#     def sleep(self):
#         print("I can sleep!")


# # derived class
# class Dog(Animal):

#     def bark(self):
#         print("I can bark! Woof woof!!")


# # Create object of the Dog class
# dog1 = Dog()

# # Calling members of the base class
# dog1.eat()
# dog1.sleep()

# # Calling member of the derived class
# dog1.bark()


class Computer:

    def __init__(self, name="Test Name"):
        self.__maxprice = 900
        self.name = name

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def set_max_price(self, price):
        self.__maxprice = price


c = Computer()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.set_max_price(1000)
c.sell()
