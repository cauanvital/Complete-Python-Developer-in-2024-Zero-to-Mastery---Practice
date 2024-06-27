# By using list comprehension, please write a program to print the list after
# removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

l1 = [12,24,35,70,88,120,155]
l2 = [j for (i,j) in enumerate(l1) if i not in [0,4,5]]
print(l2)
