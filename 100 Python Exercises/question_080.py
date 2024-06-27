# Please write a program to print the list after removing even numbers in
# [5,6,77,45,22,12,24].

l = list(filter(lambda x: x % 2 != 0, [5,6,77,45,22,12,24]))
print(l)
