# Pure Functions

def odd_numbers(even_list):
    odd_list = []
    for item in even_list:
        odd_list.append(item - 1)
    return odd_list


# even list
even_list = [2, 4, 6, 8]
print(odd_numbers(even_list))


# NOT PURE
odd_list1 = [0,9]
def odd_numbers1(even_list):

    for item in even_list:
        odd_list1.append(item - 1)
    return odd_list1


# even list
even_list1 = [2, 4, 6, 8]
print(odd_numbers1(even_list1))
