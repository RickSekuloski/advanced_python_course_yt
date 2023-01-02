# List Comprehension
# list = [expression for item in iterable if condition == True]

# first list
first_list = [2, 4, 6, 8]
# second list
second_list = []

for num in first_list:
    second_list.append(num)

print(second_list)

# list compre.... example 1
second_list2 = [num for num in first_list]
print(second_list2)

# even list example 2
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = [num for num in old_list if num % 2 == 0]
print(even_list)

# example 3
long_list = [num for num in range(0, 100)]
print(long_list)

# example 4 odd list
# odd_list = [num for num in even_list]
# odd_list = [num - 1 for num in even_list]
odd_list = [num - 1 for num in even_list if num >=3]

print(odd_list)