import random as r

def RollDice(sides = 6, throws = 1):
    rolls = []
    for i in range(throws):
        rolls.append(r.randint(1,sides))
    
    return rolls

