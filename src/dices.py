import random

def roll_single_dice():
    return random.randint(1, 6)

def roll_dices():
    """
    Roll two dices
    >>> roll_dices()
    """
    return roll_single_dice(), roll_single_dice()
