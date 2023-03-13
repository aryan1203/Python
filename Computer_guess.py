import random

def comp_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess=low
        feedback=input(f'Is {guess} to high (h),low(l),or correct(c): ')
        if feedback =='h':
            high=guess-1
        elif feedback == 'l':
            low=guess+1
            
    print(f'Congrats. Computer guessed the number ,{guess},correctly!!.')

comp_guess(20)