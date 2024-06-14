from time import time

t = time()

# execution time: 1.7033038139343262
def fib(n):
    fib = [None,0,1]
    for i in range(n + 1):
        yield fib[1]
        fib[0] = fib[1]
        fib[1] = fib[2]
        fib[2] = fib[0] + fib[1]

for i in fib(5000):
    print(i)
    
print(f'execution time: {time() - t}')
