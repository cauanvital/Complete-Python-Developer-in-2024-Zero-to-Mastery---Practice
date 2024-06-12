some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dup = list({i for i in some_list if some_list.count(i) > 1})

print(dup)
