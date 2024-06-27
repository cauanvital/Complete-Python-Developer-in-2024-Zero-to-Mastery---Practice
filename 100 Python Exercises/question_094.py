# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads
# and 94 legs among the chickens and rabbits in a farm. How many rabbits and
# how many chickens do we have?

def animal_calculator(head_qt:int=35, leg_qt:int=94):
    a = 1
    b = head_qt - 1
    
    for i in range(head_qt):
        if a + b == head_qt and 2 * a + 4 * b == leg_qt:
            return a,b
        else:
            a += 1
            b -= 1
    return 'Impossible case'
            
result = animal_calculator(1,22)
if result != 'Impossible case':
    print(f'Chickens: {result[0]}\nRabbits: {result[1]}')
else:
    print(result)
