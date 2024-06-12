def check_driver_age():
    age = int(input('What is your age? '))
    if age < 18:
        print('Sorry, you are too young to drive this car. Powering off')
    elif age == 18:
        print('Congratulations on your first year of driving. Enjoy the ride!')
    else:
        print('Powering On. Enjoy the ride!')
    
check_driver_age()

def check_driver_age(age:int = 0):
    if age < 18:
        print('Sorry, you are too young to drive this car. Powering off')
    elif age == 18:
        print('Congratulations on your first year of driving. Enjoy the ride!')
    else:
        print('Powering On. Enjoy the ride!')
    
check_driver_age()
check_driver_age(15)
check_driver_age(18)
check_driver_age(26)
