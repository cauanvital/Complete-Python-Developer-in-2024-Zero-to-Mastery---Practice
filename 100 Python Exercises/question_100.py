# You are given words. Some words may repeat. For each word, output its number
# of occurrences. The output order should correspond with the input order of
# appearance of the word. See the sample input/output for clarification.
# 
# If the following string is given as input to the program:
#   4
#   bcdef
#   abcdefg
#   bcde
#   bcdef
# 
# Then, the output of the program should be:
#   3
#   2 1 1

word_counter = {}
n = int(input())

for i in range(n):
    word = input()
    if word not in word_counter.keys():
        word_counter[word] = 1
    else:
        word_counter[word] += 1
        
print(len(word_counter))
print(*word_counter.values())
