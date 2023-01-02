# Append to a file

# with open('text.txt', mode='a') as result:
#     # print(result.read())
#     content = result.write(' My name is Rick, what is yours?')


with open('file.txt', mode='w') as result:
    # print(result.read())
    content = result.write('New Content')

with open('file1.txt', mode='a') as result:
    # print(result.read())
    content = result.write('New Content1')

with open('file2.txt', mode='r+') as result:
    # print(result.read())
    content = result.write('New Content1')
