# Given 2 sets of integers, M and N, print their symmetric difference in
# ascending order. The term symmetric difference indicates those values that
# exist in either M or N but do not exist in both.
# 
# The first line of input contains an integer, M.The second line contains M
# space-separated integers.The third line contains an integer, N.The fourth
# line contains N space-separated integers.
#   4
#   2 4 5 9
#   4
#   2 4 11 12
# 
# Output the symmetric difference integers in ascending order, one per line.
#   5
#   9
#   11
#   12

m = set(map(int,input().split()))
n = set(map(int,input().split()))

diference = list(m ^ n)
diference.sort()

print(*diference, sep='\n')
