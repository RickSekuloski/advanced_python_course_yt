# Python from-import *
import utility1
from utility import sum_fn, div_fn, mult_fn, sub_fn
from exp.pow_module import pow_fn
from exp.extra_functions.modulo_fun import modulo_fn
from utility1 import *
num1 = 6
num2 = 4
print('Utility1 outputs')
print(utility1.sum_fn1(num1, num2))
print(utility1.sub_fn1(num1, num2))
print(utility1.div_fn1(num1, num2))
print(utility1.mult_fn1(num1, num2))
print('Utility outputs')
sum_result = sum_fn(num1, num2)
sub_result = sub_fn(num1, num2)
div_result = div_fn(num1, num2)
mult_result = mult_fn(num1, num2)
pow_result = pow_fn(num1)
modulo_result = modulo_fn(num1, num2)

print(sum_result)
print(sub_result)
print(div_result)
print(mult_result)
print(pow_result)
print(modulo_result)



