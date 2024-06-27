# Given the participants' score sheet for your University Sports Day, you are
# required to find the runner-up score. You are given scores. Store them in a
# list and find the score of the runner-up.
# 
# If the following string is given as input to the program:
#   5
#   2 3 6 6 5
# 
# Then, the output of the program should be:
#   5

scores = [int(i) for i in input().split()]

scores_1 = scores.copy()
winner = max(scores_1)
for i in range(scores_1.count(winner)): scores_1.remove(winner)
print(max(scores_1))

scores_2 = list(set(scores.copy()))
scores_2.sort()
print(scores_2[-2])
