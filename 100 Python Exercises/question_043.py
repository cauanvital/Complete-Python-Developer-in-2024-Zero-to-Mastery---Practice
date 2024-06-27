# Write a program which can filter() to make a list whose elements are even
# number between 1 and 20 (both included).

filter_list = list(filter(lambda n:n % 2 == 0, range(1, 21)))
print(filter_list)
