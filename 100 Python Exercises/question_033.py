# Define a function which can generate and print a list where the values are
# square of numbers between 1 and 20 (both included).

def square_list():
    square_list = [i**2 for i in range(1,21)]
    print(square_list)
    
square_list()
