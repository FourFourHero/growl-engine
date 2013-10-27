from dice import roll_d6

def roll_attribute_score(player):
    roll = -1

    rolls = []
    rolls.append(roll_d6())
    rolls.append(roll_d6())
    rolls.append(roll_d6())
    rolls.append(roll_d6())
    rolls.sort()

    lowest_roll = rolls[0]
    second_lowest_roll = rolls[1]
    highest_roll = rolls[3]

    roll = lowest_roll + second_lowest_roll + highest_roll

    # TODO take into account traits

    return roll