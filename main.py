# iterator
class PowerTwo:
    def __init__(self, max_number):
        self.n = 0
        self.max_number = max_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max_number:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result


p = PowerTwo(10)
print("Pow func using iter: ", p.__next__())
print("Pow func using iter: ", p.__next__())
print("Pow func using iter: ", p.__next__())

print("-------------------------------------")


# generator function
def power_generator(max_number):
    n = 0
    while n < max_number:
        yield 2 ** n
        n += 1


pf = power_generator(10)
print("Generator pow func: ", next(pf))
print("Generator pow func: ", next(pf))
print("Generator pow func: ", next(pf))

print("-------------------------------------")


# infinite generator function
def even_number():
    n = 2
    while True:
        yield n
        n += 2


even = even_number()
print("Even : ", next(even))
print("Even : ", next(even))
print("Even : ", next(even))
print("Even : ", next(even))
print("Even : ", next(even))

print("-------------------------------------")


# pipelining generator function practice
def fab_number(numbers):
    x, y = 0, 1
    for _ in range(numbers):
        x, y = y, x + 2
        yield x


def sqrt(numbers):
    for number in numbers:
        yield number ** 2


print("Sum of sqrt of fab number (Pipelining Generators) : ", sum(sqrt(fab_number(10))))
