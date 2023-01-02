# Set and Dictionary Comprehension
# list = [expression for item in iterable if condition == True]

# first set
first_set = {10, 12, 14, 16}
# second set
second_set = {}

# set compre...
second_set = {num for num in first_set}
print(second_set)

# example 2
long_set = {num for num in range(0, 100)}
print(long_set)

# Dictionary
my_dict1 = {
    'one': 1,
    'two': 2,
    'three': 3
}
# my_dict2 = {key:value for key,value in my_dict1.items()}
# my_dict2 = {key:value+1 for key,value in my_dict1.items()}
my_dict2 = {key:value for key,value in my_dict1.items() if value % 2 == 0}

print(my_dict2)