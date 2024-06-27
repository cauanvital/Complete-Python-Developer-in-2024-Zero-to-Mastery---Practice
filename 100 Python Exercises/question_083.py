# By using list comprehension, please write a program to print the list after
# removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

l1 = [12,24,35,70,88,120,155]
l2 = [i for (j,i) in enumerate(l1) if j not in [2,4]]
print(l2)
