# Please write a program to output a random even number between 0 and 10
# inclusive using random module and list comprehension.

from random import randrange

n = randrange(0, 11, 2)
print(n)
