# By using list comprehension, please write a program to print the list after
# removing the value 24 in [12,24,35,24,88,120,155].

l1 = [12,24,35,24,88,120,155]
l2 = [i for i in l1 if i != 24]
print(l2)
