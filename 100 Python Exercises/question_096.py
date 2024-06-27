# You are given a string S and width W. Your task is to wrap the string into a
# paragraph of width.
# 
# If the following string is given as input to the program:
#   ABCDEFGHIJKLMNOPQRSTUVWXYZ
#   4
# 
# Then, the output of the program should be:
#   ABCD
#   EFGH
#   IJKL
#   IMNO
#   QRST
#   UVWX
#   YZ

def paragraph_maker(s,w):
    for i in range(round(len(s) / w + 0.5)):
        print(s[:w])
        s = s[w:]
        
string = input()
width = int(input())
paragraph_maker(string, width)
