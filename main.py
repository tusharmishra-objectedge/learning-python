# basic concepts used in python


# for loop
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

# conditionals
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is negative")


# functions
def add(x, y):
    return x + y


result = add(5, 3)
print(result)


# classes
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Fido", 5)
print(dog1.name)
print(dog1.age)

# exception handling
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# list comprehension
nums = [1, 2, 3, 4, 5]
squared_nums = [x ** 2 for x in nums]
print(squared_nums)

# lambda
double = lambda x: x * 2
result = double(5)
print(result)

# map & filter
nums = [1, 2, 3, 4, 5]
squared_nums = map(lambda x: x ** 2, nums)
filtered_nums = filter(lambda x: x > 2, squared_nums)
print(list(filtered_nums))

# dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])

# tuple
fruits = ("apple", "banana", "cherry")
print(fruits[1])

# set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# sorting
nums = [3, 1, 4, 2, 5]
nums.sort()
print(nums)


# generator
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(5)
for x in f:
    print(x, end=" ")


# decorators
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("**********")
        func(*args, **kwargs)
        print("**********")

    return wrap_func


@my_decorator
def hello(name):
    print(f"Hello, {name}")


hello("John")
