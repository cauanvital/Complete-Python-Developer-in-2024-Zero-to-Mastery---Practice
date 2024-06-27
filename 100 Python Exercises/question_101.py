# You are given a string.Your task is to count the frequency of letters of the
# string and print the letters in descending order of frequency.
# 
# If the following string is given as input to the program:
#   aabbbccde
# 
# Then, the output of the program should be:
#   b 3
#   a 2
#   c 2
#   d 1
#   e 1

string = input()
f_counter = {i:string.count(i) for i in set(string)}
sorted_counter = {i:j for i,j in sorted(f_counter.items(), key=lambda n: n[1])}

for i in list(sorted_counter.keys())[::-1]:
    print(i,sorted_counter[i])
