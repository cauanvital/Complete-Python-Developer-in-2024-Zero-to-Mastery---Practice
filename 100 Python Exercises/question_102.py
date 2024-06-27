# Write a Python program that accepts a string and calculate the number of
# digits and letters.
# 
# Input
#   Hello321Bye360
# 
# Output
#   Digit - 6
#   Letter - 8

string = input()
digit_count = 0
alpha_count = 0

for i in string:
    if i.isdigit():
        digit_count += 1
    elif i.isalpha():
        alpha_count += 1
        
print(f'Digit - {digit_count}')
print(f'Letter - {alpha_count}')
