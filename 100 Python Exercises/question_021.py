# A robot moves in a plane starting from the original point (0,0). The robot
# can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of
# robot movement is shown as the following:
#   UP 5
#   DOWN 3
#   LEFT 3
#   RIGHT 2
# 
# The numbers after the direction are steps. Please write a program to compute
# the distance from current position after a sequence of movement and original
# point. If the distance is a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:
#   UP 5
#   DOWN 3
#   LEFT 3
#   RIGHT 2
# 
# Then, the output of the program should be:
#   2

def distance_from_0_0(x, y):
    var = (0 - x) ** 2 + (0 - y) ** 2
    if var < 0:
        var *= -1
    return round(var ** 0.5)

position = [0,0]

while True:
    move = input().upper().split()
    if not move:
        break
    
    move[1] = int(move[1])
    if move[0] == 'UP':
        position[1] += move[1]
    elif move[0] == 'DOWN':
        position[1] -= move[1]
    elif move[0] == 'LEFT':
        position[0] -= move[1]
    elif move[0] == 'RIGHT':
        position[0] += move[1]
        
    
print(distance_from_0_0(*position))
