def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add(1, 2))

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)