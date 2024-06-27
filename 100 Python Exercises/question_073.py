# Please write a program to randomly generate a list with 5 even numbers
# between 100 and 200 inclusive.

from random import randrange

my_list = [randrange(100, 201, 2) for i in range(5)]
print(my_list)
