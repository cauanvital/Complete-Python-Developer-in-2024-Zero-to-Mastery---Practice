# Please write assert statements to verify that every number in the list
# [2,4,6,8] is even.

my_list = [2,4,6,8]

for i in my_list:
    assert i % 2 == 0, f'{i} is not an even number'
