# square
my_list = [5, 4, 3]
print(list(map(lambda n: n ** 2, my_list)))

# list sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda n: n[1])
print(a)
