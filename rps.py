import random

def play():
    user=input("'r' for rock, 'p' for paper, 's' for scissors\n Enter your Choice ::")
    computer =random.choice(['r','p','s'])
    
    if user == computer :
        return "It's a Tie"
    
    if is_win(user,computer):
        return "You Won!!"
    
    return "You Lost!!"

def is_win(player,opponent):
    if (player =='r' and opponent == 's') or (player =='p' and opponent == 'r') or (player =='s' and opponent == 'p'):
        return True

result='y'
while(result=='y' or result=='Y'):
    print(play())
    result=input("Do you want to play Again? : ")[0]