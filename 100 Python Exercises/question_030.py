# Define a function that can accept two strings as input and print the string
# with maximum length in console. If two strings have the same length, then the
# function should print all strings line by line.

def greater_str(*args):
    greater_str = ['']
    for string in args:
        if len(string) > len(greater_str[0]):
            greater_str = [string]
        elif len(string) == len(greater_str[0]):
            greater_str.append(string)
    
    print(*greater_str, sep='\n')

greater_str('abc','defghi','jk','lmnopq')
