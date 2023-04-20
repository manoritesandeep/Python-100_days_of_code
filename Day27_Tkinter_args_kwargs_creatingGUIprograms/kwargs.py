# Any number of keyword arguments

def calculate(n, **kwargs):
    # print(type(kwargs)) # dict
    # for key,value in kwargs:
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=2, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")


my_car = Car(make="Rivian", model="R1S")
print(my_car.make)
print(my_car.model)
print(my_car.colour)


