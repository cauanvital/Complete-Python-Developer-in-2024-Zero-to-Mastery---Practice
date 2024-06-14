# Write a program that accepts a sentence and calculate the number of upper
# case letters and lower case letters.
# 
# Suppose the following input is supplied to the program:
#   Hello world!
# 
# Then, the output should be:
#   UPPER CASE 1
#   LOWER CASE 9

sentence = input()
upper = len(list(filter(lambda i:str(i).isupper(), sentence)))
lower = len(list(filter(lambda i:str(i).islower(), sentence)))

print(f'UPPER CASE {upper}\nLOWER CASE {lower}')
