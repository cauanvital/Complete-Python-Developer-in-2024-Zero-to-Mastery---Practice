# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first
# half values in one line and the last half values in one line.

my_tuple = (1,2,3,4,5,6,7,8,9,10)
tuple_mid = len(my_tuple) // 2

print(my_tuple[:tuple_mid])
print(my_tuple[tuple_mid:])
