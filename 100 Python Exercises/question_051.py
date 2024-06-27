# Write a function to compute 5/0 and use try/except to catch the exceptions.

try:
    5/0
except ZeroDivisionError:
    print('Can\'t divide number by 0')
except:
    print('An exception raised and I don\'t know why')
