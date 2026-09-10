import math
print(dir(math))

from math import e, exp, log

print(pow(e, 1))
print(pow(2, 2))
print(log(e, e))
print(exp(log(e)))
print(exp(2 * log(2)))
print(exp(0))

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
