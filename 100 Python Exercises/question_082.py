# By using list comprehension, please write a program to print the list after
# removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

l1 = [12,24,35,70,88,120,155]
l2 = [l1[i] for i in range(1,len(l1),2)]
print(l2)
