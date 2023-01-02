# Filter Function
# help(filter)

# function
def only_even_nums(list_item):
    return list_item % 2 == 0


# numbers list
numbers_list = [1, 2, 3, 4, 5, 6]
# filter function
print(list(filter(only_even_nums, numbers_list)))


# fuction
def filter_names(list_item):
    return 'om' in list_item


# user names
user_names = ['Tom', 'Shanon', 'Jason', 'Antom', 'Andy', 'Carol']

# filter fun
print(list(filter(filter_names, user_names)))

