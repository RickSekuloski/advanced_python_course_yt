# Handling Errors - Finally block

def d_fn(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError) as err:
        print(f'An Error! {err}')
    finally:
        print('This block will run')


result = d_fn(10, 2)
print(result)
