# Error Handling: Try - Except Block
# with open('./scripts/test.txt', mode='r') as result:
#     print(result.read())
try:
    with open('./scripts/test.txt', mode='r') as result:
        print(result.read())
except FileNotFoundError as err:
    print('File Was Not Found!')
    print(err)
    # raise err
except IOError as err1:
    print('IOError!')
    print(err1)
print('This comes after the try-except block')

# ImportError
# IndexError
# TypeError
