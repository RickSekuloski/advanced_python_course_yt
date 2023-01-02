# Python Packages and Modules
# Python from-import
# import utility
from utility import sum_fn, div_fn, mult_fn, sub_fn
# import exp.pow_module
from exp.pow_module import pow_fn
# import exp.extra_functions.modulo_fun
from exp.extra_functions.modulo_fun import modulo_fn
# print(exp.pow_module)
num1 = 6
num2 = 4

# sum_result = utility.sum_fn(num1, num2)
# sub_result = utility.sub_fn(num1, num2)
# div_result = utility.div_fn(num1, num2)
# mult_result = utility.mult_fn(num1, num2)
# pow_result = exp.pow_module.pow_fn(num1)

sum_result = sum_fn(num1, num2)
sub_result = sub_fn(num1, num2)
div_result = div_fn(num1, num2)
mult_result = mult_fn(num1, num2)
# pow_result = exp.pow_module.pow_fn(num1)
pow_result = pow_fn(num1)
# modulo_result = exp.extra_functions.modulo_fun.modulo_fn(num1, num2)
modulo_result = modulo_fn(num1, num2)

print(sum_result)
print(sub_result)
print(div_result)
print(mult_result)
print(pow_result)
print(modulo_result)



