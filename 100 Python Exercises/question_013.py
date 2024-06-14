# Write a program that accepts a sentence and calculate the number of letters
# and digits.
# 
# Suppose the following input is supplied to the program:
#   hello world! 123
# 
# Then, the output should be:
#   LETTERS 10
#   DIGITS 3

sentence = input()
letters = len(list(filter(lambda i:str(i).isalpha(), sentence)))
digits = len(list(filter(lambda i:str(i).isdigit(), sentence)))

print(f'LETTERS {letters}\nDIGITS {digits}')
