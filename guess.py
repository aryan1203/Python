import random

def guess(x):
    random_numb=random.randint(1,x)
    guessvari=0
    while guessvari!=random_numb:
        guessvari=int(input(f'Guess a number between 1 and {x}: '))
        if guessvari<random_numb:
            print("Sorry, guess again. Too low.")
        elif guessvari>random_numb:
            print("Sorry, guess again. Too high.")
            
    print(f'Congrats. You have guessed the number {guessvari}')
value=int(input('Enter the range: '))
guess(value)