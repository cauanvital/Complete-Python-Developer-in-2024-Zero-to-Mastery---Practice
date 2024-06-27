# Please write a program which prints all permutations of [1,2,3]

from itertools import permutations

my_list = [1,2,3]
print(*permutations(my_list), sep='\n')
