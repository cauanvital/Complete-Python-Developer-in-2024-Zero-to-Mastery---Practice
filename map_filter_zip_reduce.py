from functools import reduce

#1 Capitalize all of the pet names and print the list

my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_list(word:str):
    return word.capitalize()

print(list(map(capitalize_list, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(sorted(my_numbers), my_strings)))

#3 Filter the scores that pass over 50%

scores = [73, 20, 65, 19, 76, 100, 88]

def filter_greater_than_50(n):
    return n > 50

print(list(filter(filter_greater_than_50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, my_numbers + scores))
