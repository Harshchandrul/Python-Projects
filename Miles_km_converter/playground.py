# Learning about args and kwargs

# def add(*args):
#     print(args[0])
#     sum_n = 0
#     for n in args:
#         sum_n += n
#     return sum_n
#
#
# a = add(1, 2, 3, 5)
# print(a)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(5, add=3, multiply=5)

# To use kwargs in class


class Cars:
    def __init__(self, **kw):
        self.make = kw['make']
        # It can give us error if the user doesn't pass model attribute
        # but we can use .get() to avoid that and that will return none
        self.model = kw.get("model")


car = Cars(make="Nissan", model="GT-R")
print(car.model)
print(car.make)
