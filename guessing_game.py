from random import randint

number = randint(1,10)

def guess_validator():
    guess = input('Take a guess 1~10: ')
    try:
        guess = int(guess)
        if guess > 0 and guess < 11:
            return guess
    except:
        pass
    print('Invalid')
    guess_validator()

def guess_checker(guess, answer):
    return guess == answer

def guess_number():
    number = randint(1,10)
    
    while True:
        guess = guess_validator()
        if guess_checker(guess, number):
            print('Right')
            break
        print('Wrong')
