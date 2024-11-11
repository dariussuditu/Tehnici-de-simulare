import random
import numpy as np

def roll_dice():
    return [(random.randint(1, 6), random.randint(1, 6)), (random.randint(1, 6), random.randint(1, 6))]

def simulate_game():
    player, opponent = roll_dice()

    while player == opponent:
        player, opponent = roll_dice()

    if player == (1, 1) and opponent != (1, 1):
        return True

    elif opponent == (1, 1) and player != (1, 1):
        return False

    elif player != (1, 1) and opponent != (1, 1):
        if player in {(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)} and opponent in {(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)}:
            if sum(player) > sum(opponent):
                return True
            elif sum(player) < sum(opponent):
                return False
            
        
        elif player in {(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)} and opponent not in {(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)}:
            return True
        
        elif opponent in {(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)} and player not in {(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)}:
            return False
        
        elif player not in {(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)} and opponent not in {(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)}:

            if sum(player) > sum(opponent):
                return True
            elif sum(player) < sum(opponent):
                return False
            else:

                return simulate_game()

def win_probability(n=100000):
    win = 0
    for _ in range(n):
        if simulate_game():
            win += 1
    
    win_rate = win / n
    return win_rate

print(f"Probabilitatea estimata de castig: {win_probability():.4f}")
