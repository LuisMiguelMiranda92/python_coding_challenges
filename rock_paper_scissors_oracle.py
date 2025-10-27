"""
You are the rock paper scissors oracle.

Famed throughout the land, you have the incredible ability to predict which hand gestures your opponent will choose out of rock, 
paper and scissors.

Unfortunately you're no longer a youngster, and have trouble moving your hands between rounds. 
For this reason, you can only pick a single gesture for each opponent. If it's possible for you to win, you will, 
but you're also happy to tie.

Given an array of gestures — for example ["paper", "scissors", "scissors"] — return the winning gesture/s in the order 
in which they appear in the title, separated by a forward slash. 
For example, if rock and scissors could both be used to win you would return:

"rock/scissors"

If it's not possible for you to win then return:

"tie"
"""
def oracle(gestures):
    #work your magic here
    r, p, s = 0, 0, 0
    
    for gesture in gestures:
        if gesture == 'rock':
            p += 1
            s -= 1
        elif gesture == 'paper':
            s += 1
            r -= 1
        elif gesture == 'scissors':
            r += 1
            p -= 1
            
    if (r == p and r == s):
        return 'tie'
    
    if r > 0 and p <= 0 and s <= 0:
        return 'rock'
    elif r <= 0 and p > 0 and s <= 0:
        return 'paper'
    elif r <= 0 and p <= 0 and s > 0:
        return 'scissors'
    elif r > 0 and p > 0:
        return 'rock/paper'
    elif r > 0 and s > 0:
        return 'rock/scissors'
    elif p > 0 and s > 0:
        return 'paper/scissors'