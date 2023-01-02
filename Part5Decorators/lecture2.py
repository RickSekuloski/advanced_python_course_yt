# Decorators

# decorator example
def decorator_function(func):
    def wrapper_fn():
        print('*** What is your name? ***')
        func()
        print('*** Thank you! ***')
    return wrapper_fn

@decorator_function
def my_name():
    print('My name is Rick')

my_name()

# a = decorator_function(my_name)
# print(a)

# example 2
# decorator example
def decorator_function1(func):
    def wrapper_fn(name):
        print('*** What is your name? ***')
        func(name)
        print('*** Thank you! ***')
    return wrapper_fn

@decorator_function1
def my_name1(name):
    print(f'My name is {name}')

my_name1('John Doe')