# Handling Multiple Errors

def d_fn(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError) as err:
        print(f'An Error! {err}')
    # except ZeroDivisionError as err:
    #     print(f'Make sure both operands are not zero! {err}')

# result = d_fn(10, 5)
result = d_fn(10, '5')
# result = d_fn(10, 0)
print(result)
