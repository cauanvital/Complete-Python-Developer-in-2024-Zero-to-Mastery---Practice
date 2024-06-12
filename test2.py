from datetime import datetime

t = datetime.now()
def a(n):
    return (n + 1) * 2

j = 0

for i in range(100000000):
    j = a(i)

print(j)
print(f'Execution time: {datetime.now() - t}')
