# Write a program which can compute the factorial of a given numbers.The
# results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output
# should be:40320

def factorial(n):
    for i in range(1, n):
        n *= i
    return n
        
numbers = [int(input('insert a number: '))]
print(*list(map(factorial, numbers)), sep=', ')
