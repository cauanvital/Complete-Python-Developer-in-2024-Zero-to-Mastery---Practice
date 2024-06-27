# Please write a program to print the running time of execution of "1+1" for
# 100 times.

from time import time

t_before = time()
for i in range(100): 1 + 1
print(time() - t_before)
