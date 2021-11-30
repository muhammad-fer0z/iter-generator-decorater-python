"""
Here is some practice of python custom decorator.
Decorator help us to wrapper outside the function.
When decorator pass the value then other function
will execute.
"""


# Integer number checker decorator
def check_number_is_int(func):
    def inner(a, b):
        print("Value a({}) add with value b({}).".format(a, b))
        if type(a) is int and type(b) is int:
            return func(a, b)
        else:
            print("Only take\'s whole number")
            return 0

    return inner


# decorator for checking given number is greater then zero
def is_greater_then_zero(func):
    def inner(a, b):
        if a < 0 or b < 0:
            print("We can\'t add both value of a({}) and b({}) because values always greater then zero.".format(a, b))
            return 0
        return func(a, b)

    return inner


# decorators
@check_number_is_int
@is_greater_then_zero
def add(a, b):
    return a + b


val = add(3, -87)
print("Sum : ", val)
