# *args, **kwargs and Decorators


# decorator example
def decorator_function2(func):
    def wrapper_fn(*args, **kwargs):
        print('*** What is your name? ***')
        func(*args, **kwargs)
        print('*** Thank you! ***')

    return wrapper_fn


@decorator_function2
def my_name2(name, work='Programmer', lives='USA'):
    print(f'My name is {name}, {work}, {lives}')


my_name2('John Doe')
