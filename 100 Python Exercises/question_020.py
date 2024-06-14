# Define a class with a generator which can iterate the numbers, which are
# divisible by 7, between a given range 0 and n.
# 
# Suppose the following input is supplied to the program:
#   7
# 
# Then, the output should be:
#   0
#   7
#   14

class SevenMultipliers:
    def __init__(self, end:int,*, start:int=0):
        self._first_iteration = True
        self._current = start
        self._end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._first_iteration:
            self._first_iteration = False
            if self._current % 7 != 0:
                while self._current % 7 != 0:
                    self._current += 1
                    
            if self._current > self._end:
                raise StopIteration
            
            return self._current
        else:
            self._current += 7
            
            if self._current > self._end:
                raise StopIteration
            
            return self._current

number = int(input())
for i in SevenMultipliers(number):
    print(i)

