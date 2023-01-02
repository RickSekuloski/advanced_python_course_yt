# Generators Intro

# mylist = [1, 2, 3, 4, 5]
# print(mylist)
# print(mylist[0])
# print(mylist[1])

def our_generator(n):
    for i in range(n):
        yield i

# for item in our_generator(5):
#     print(item)

item = our_generator(3)
print(next(item))
print(next(item))
print(next(item))
# print(next(item))