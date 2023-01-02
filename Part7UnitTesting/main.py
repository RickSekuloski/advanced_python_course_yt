# PART 7 - UNIT TESTING

def multiply_by_7(x):
    try:
        if x != None:
            return int(x) * 7
        else:
            # return 0
            return 'None is not allowed, please use number next time'
    except ValueError as err:
        return err

