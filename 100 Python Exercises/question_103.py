# Given a number N.Find Sum of 1 to N Using Recursion
# 
# Input
#   5
# 
# Output
#   15

def sum_n(n):
    if n == 0:
        return n
    return sum_n(n - 1) + n

num = int(input())
print(sum_n(num))
