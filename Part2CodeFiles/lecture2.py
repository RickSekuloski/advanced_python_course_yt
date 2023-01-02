# Write to a file
# with open('text.txt', mode='r') as result:
#     # print(result.read())

# with open('text.txt', mode='w') as result:
#     # print(result.read())
#     result.write('Hi there')

with open('text.txt', mode='r+') as result:
    # print(result.read())
    content = result.write('Hi there!')
