# Write a program which can map() to make a list whose elements are square of
# numbers between 1 and 20 (both included).

map_list = list(map(lambda n:n**2, range(1,21)))
print(map_list)
