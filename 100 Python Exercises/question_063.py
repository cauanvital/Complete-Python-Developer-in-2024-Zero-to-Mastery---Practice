# Please write a program using generator to print the even numbers between 0
# and n in comma separated form while n is input by console.
# 
# Example: If the following n is given as input to the program:
#   10
# 
# Then, the output of the program should be:
#   0,2,4,6,8,10
# 
# In case of input data being supplied to the question, it should be assumed to
# be a console input.

class EvenGenerator:
    def __init__(self, *args):
        self._start = 0 if len(args) == 1 else args[0]
        self._end = args[0] if len(args) == 1 else args[1]
        self._actual = self._start
        self._is_first_iteration = True
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._is_first_iteration:
            self._is_first_iteration = False
            self._actual += 1 if self._actual % 2 != 0 else 0
            if self._actual > self._end:
                raise StopIteration
            return self._actual
        
        self._actual += 2
        
        if self._actual > self._end:
            raise StopIteration
        
        return self._actual

n = int(input())
print(*EvenGenerator(n), sep=',')
