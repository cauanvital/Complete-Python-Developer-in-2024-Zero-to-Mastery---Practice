# Write a program, which will find all such numbers between 1000 and 3000 (both
# included) such that each digit of the number is an even number.The numbers
# obtained should be printed in a comma-separated sequence on a single line.

def have_even_digit(n):
    n = str(n)
    odd_counter = 0
    for i in n:
        if int(i) % 2 != 0:
            odd_counter += 1
    return odd_counter == 0

only_even = list(filter(have_even_digit,range(1000, 3001)))
print(*only_even, sep=',')
