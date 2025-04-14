import random

def play():
    user = input("Enter a choice (rock, paper, scissors): ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return "You win!"
    
    return "You Lost!"

def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or \
        (player == 'scissors' and opponent == 'paper') or \
        (player == 'paper' and opponent == 'rock'):
        return True
    
print(play())