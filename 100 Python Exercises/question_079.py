# Please write a program to generate all sentences where subject is in
# ["I", "You"] and verb is in ["Play", "Love"] and the object is in
# ["Hockey","Football"].

from numpy import prod

class CombinationGenerator:
    def __init__(self, *args):
        self._first_iter = True
        self._lists = args[0] if len(args) == 1 else args
        self._list_sz = len(self._lists)
        self._state = [[i,0] for i in [len(i) for i in self._lists]]
        
        self._actual = -1
        self._end = prod([len(i) for i in self._lists])
        
    @property
    def sentence(self):
        transform = lambda x: str(self._lists[x][self._state[x][1]])
        return ' '.join([transform(i) for i in range(self._list_sz)])
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self._actual += 1
        if self._actual >= self._end:
            raise StopIteration
        
        if self._first_iter:
            self._first_iter = False
            return self.sentence
        self.__change_combination__()
        
        return self.sentence
    
    def __change_combination__(self, gear=0):
        if gear >= len(self._state):
            pass
        elif self._state[gear][0] - 1 != self._state[gear][1]:
            self._state[gear][1] += 1
        else:
            self._state[gear][1] = 0
            self.__change_combination__(gear + 1)

lists = [
    ['I', 'You'],
    ['Play', 'Love'],
    ['Hockey', 'Football']
]

for i in CombinationGenerator(lists):
    print(i)
    
# Ah, sh**... I actually tried to make a responsive generator that would accept
# any number of lists and lists of any size, and then return all possible
# combinations of those lists... I don't know if I should have spent so much
# time on this, but I think I'm satisfied with the result lol
