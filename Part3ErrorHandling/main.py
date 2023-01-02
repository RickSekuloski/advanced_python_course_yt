# Raise an error

def d_fn(a, b):
    try:
        if b == 1:
            raise Exception('The Second Operand (b) should be bigger than 1!')
        return a / b
    except (TypeError, ZeroDivisionError, Exception) as err:
        print(f'An Error! {err}')
    finally:
        print('This block will run')


result = d_fn(8, 1)
print(result)
