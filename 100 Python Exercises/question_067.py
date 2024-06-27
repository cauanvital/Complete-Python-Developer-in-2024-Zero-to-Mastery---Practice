# Please write a binary search function which searches an item in a sorted
# list. The function should return the index of element to be searched in the
# list.

def bin_search(li, element):
    low_pos = 0
    top_pos = len(li) - 1
    
    while low_pos <= top_pos:
        mid_pos = (low_pos + top_pos) // 2
            
        if li[mid_pos] == element:
            return mid_pos
        elif li[mid_pos] < element:
            low_pos = mid_pos + 1
        else:
            top_pos = mid_pos - 1

li = [1,2,3,4,5,6,7,8,9]
li.sort()

print(bin_search(li, 0))
print(bin_search(li, 7))
