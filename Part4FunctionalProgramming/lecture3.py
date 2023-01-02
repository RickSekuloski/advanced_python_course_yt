# Map() function
# help(map)

def odd_numbers(list_item):
    return list_item - 1


# even list
even_list = [2, 4, 6, 8]

print(list(map(odd_numbers, even_list)))
print(even_list)


# map example 2
def user_names(user_item):
    return user_item.upper()

# user list
user_list = ['andy', 'tom', 'carol']

print(list(map(user_names, user_list)))