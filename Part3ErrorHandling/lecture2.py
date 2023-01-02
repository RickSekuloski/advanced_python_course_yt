# Error Handling
x = 9
while True:
    try:
        user_num = int(input('Please Enter a Number: '))
        print(user_num + x)
    except:
        print('Please Enter a Number Not a String')

    else:
        break

print('Hi')