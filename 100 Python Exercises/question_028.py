# Define a function that can receive two integer numbers in string form and
# compute their sum and then print it in console

def sum_str_numbers(n1:str, n2:str):
    n = int(n1) + int(n2)
    print(n)
    return n

sum_str_numbers('1', '2')
