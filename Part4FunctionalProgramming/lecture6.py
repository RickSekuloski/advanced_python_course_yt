# Reduce function
from functools import reduce

# numbers list
num_list = [1, 2, 3, 4, 5]


def accumulator(acc, item):
    # print(acc)
    # print(item)
    print(f'Acc: {acc}, item: {item}')
    return acc + item

#1st pass: 1
#2nd pass: 3
#3rd pass: 6
#4th pass: 10
#5th pass: 15

print(reduce(accumulator, num_list, 0))
# link
# https://docs.python.org/3/library/functools.html
