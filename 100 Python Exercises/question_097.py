# You are given an integer, N. Your task is to print an alphabet rangoli of
# size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
# 
# Different sizes of alphabet rangoli are shown below:
#   #size 3
# 
#   ----c----
#   --c-b-c--
#   c-b-a-b-c
#   --c-b-c--
#   ----c----
# 
#   #size 5
#
#   --------e--------
#   ------e-d-e------
#   ----e-d-c-d-e----
#   --e-d-c-b-c-d-e--
#   e-d-c-b-a-b-c-d-e
#   --e-d-c-b-c-d-e--
#   ----e-d-c-d-e----
#   ------e-d-e------
#   --------e--------

class AlphabetGenerator:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    def __init__(self, n):
        self._actual = -1
        self._iter_count = -1
        self._end = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self._actual += 1
        self._iter_count += 1
        if self._iter_count >= self._end:
            raise StopIteration
        
        if self._actual >= 26:
            self._actual = 0
        return self.letters[self._actual]

def alphabet_rangoli(n):
    alpha = list(AlphabetGenerator(n))
    layers = [f'{''.join(alpha[i:n][::-1] + alpha[i:n][1:])}'.center(n * 2 - 1, '-') for i in range(n)][::-1]
    layers = layers + layers[-2::-1]
    for i in layers:
        print('-'.join(i))
    
alphabet_rangoli(35)
