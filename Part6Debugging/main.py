# PART 6 - PDB - Python Debugger
import pdb


def calc_sum(num1, num2, num3):
    # print(num1, num2, num3)
    # print(type(num1))
    # print(type(num2))
    # print(type(num3))
    # pdb.set_trace()
    return num1 + num2 + num3


result = calc_sum(1, 2, 3)
print(result)
