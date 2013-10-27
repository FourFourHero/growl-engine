import logging
import random

def roll_d6():
    roll = random.randint(1,6)
    logging.debug('roll_d6:' + str(roll))
    return roll