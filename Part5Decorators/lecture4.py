# Decorators, Examples where they can be used
from random import randint
from time import time, sleep

# def run_script():
#     t1 = time()
#     sleep(randint(1, 4))
#     t2 = time()
#     print(f'The program is finished in {t2 - t1} seconds!')
#
# run_script()

# decorator example
def execution_time(func):
    def wrapper_fn(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'The program is finished in {t2 - t1} seconds!')
    return wrapper_fn

@execution_time
def run_script():
    sleep(randint(1, 4))

# run_script()



# example 2
user = {
    'registered': True,
    'name': 'Tom',
    'email': 'tom@gmail.com'
}
# decorator example
def loggedin(func):
    def wrapper_fn(*args, **kwargs):
        # print(args[0])
        if args[0]['registered']:
            return func(*args, **kwargs)
    return wrapper_fn

@loggedin
def welcome_message(user):
    print(f"Welcome {user['name']} to our site")

welcome_message(user)