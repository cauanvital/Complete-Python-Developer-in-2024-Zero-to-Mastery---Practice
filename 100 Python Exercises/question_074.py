# Please write a program to randomly generate a list with 5 numbers, which are
# divisible by 5 and 7 , between 1 and 1000 inclusive.

from random import choice

divisor_list = [i for i in range(10, 151) if i % 5 == 0 and i % 7 == 0]
n = [choice(divisor_list) for i in range(5)]
print(n)
