# Write a program to generate and print another tuple whose values are even
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

my_tuple = (1,2,3,4,5,6,7,8,9,10)
filter_tuple = tuple(filter(lambda n:n % 2 == 0, my_tuple))
print(filter_tuple)
