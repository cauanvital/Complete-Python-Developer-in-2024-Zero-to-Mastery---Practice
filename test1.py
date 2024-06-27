class Gear:
    def __init__(self, gears_size:list[int]):
        self._current_state = [[i,0] for i in gears_size]
        self.all_states = set()
            
    def view_state(self):
        for i in self._current_state[:-1]:
            print(f'{i[0]}: {i[1]}', end=' - ')
        print(f'{self._current_state[-1][0]}: {self._current_state[-1][1]}')
            
    def round_gear(self, gear=0):
        if gear >= len(self._current_state):
            pass
        elif self._current_state[gear][0] - 1 != self._current_state[gear][1]:
            self._current_state[gear][1] += 1
        else:
            self._current_state[gear][1] = 0
            self.round_gear(gear + 1)
            
        c_state = [f'{i[0]}: {i[1]}' for i in self._current_state]
        self.all_states.add(str(c_state))

my_gear = Gear([2, 3, 5])

for i in range(100):
    my_gear.round_gear()
    my_gear.view_state()
