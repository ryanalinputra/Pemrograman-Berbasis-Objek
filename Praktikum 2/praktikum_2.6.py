from random import random

for i in range(5):
    print(random())

from random import random, seed

# seed(0)
for i in range(5):
    print(random())

from random import randrange

for i in range(10):
    print(randrange(0, 6), end=',')
print()
for i in range(10):
    print(randrange(0, 6, 2), end=',')
print()

from random import randint

for i in range(10):
    print(randint(0, 6), end=',')
print()
for i in range(10):
    print(randint(0, 6), end=',')
print()

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))
