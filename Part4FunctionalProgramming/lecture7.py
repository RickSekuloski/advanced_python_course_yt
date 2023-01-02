# Lambda expression
from functools import reduce
# lambda params: expression
num_list = [-1, 0, 1, 2, 3, 4]
#map(function, num_list)
print(list(map(lambda item: item + 1, num_list)))


# the exact same
def add_one(item):
    return item + 1

print(list(map(add_one, num_list)))

# reduce example with lambda
# reduce (func, iterable, acc)

print(reduce(lambda acc, item: acc + item, num_list, 0))