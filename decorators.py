from time import time

def performance(func):
    def performance_wrap(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(f'execution time: {time() - t}')
        
    return performance_wrap

@performance
def long_time():
    for i in range(10000000):
        i ** 2 + 123 // 5 * 3 / 70
    else:
        print(i)
        
long_time()
