# Define a function that can accept two strings as input and concatenate them
# and then print it in console

def str_concat(str1:str, str2:str,*,reverse:bool=False):
    concat_str = str1 + str2 if not reverse else str2 + str1
    print(concat_str)
    return concat_str

str_concat('abc', 'DEF')
str_concat('abc', 'DEF', reverse=True)
