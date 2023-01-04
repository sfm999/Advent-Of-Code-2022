
LHS_ROCK = ('A', 1)
LHS_PAPER = ('B', 2)
LHS_SCISSORS = ('C', 3)

THEIR_HANDS = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

OUR_HANDS = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

RHS_ROCK = ('X', 1)
RHS_PAPER = ('Y', 2)
RHS_SCISSORS = ('Z', 3)

LOSE = 0
DRAW = 3
WIN = 6

LOSE_DESIRED = 'X'
DRAW_DESIRED = 'Y'
WIN_DESIRED = 'Z'

DESIRED_OUTCOME = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

# Key is what they throw
# Value is what we need to throw to achieve outcome
WIN_LIST = {
    'A': 'Y',   # Rock     | Paper
    'B': 'Z',   # Paper    | Scissors
    'C': 'X'    # Scissors | Rock
}

LOSE_LIST = {
    'A': 'Z',   # Rock     | Scissors
    'B': 'X',   # Paper    | Rock
    'C': 'Y'    # Scissors | Paper
}

DRAW_LIST = {
    'A': 'X',   # Rock     | Rock
    'B': 'Y',   # Paper    | Paper
    'C': 'Z'    # Scissors | Scissors
}


def get_data(filename):
    with open(filename, 'r') as fr:
        data = []
        for line in fr.readlines():
            split_line = line.split(" ")
            for i in range(len(split_line)):
                split_line[i] = split_line[i].replace('\n', '')
            data.append(split_line)
    return data


def did_you_win(their_hand, my_hand):

    if my_hand == RHS_ROCK[0]:
        if their_hand == LHS_SCISSORS[0]:
            return WIN + RHS_ROCK[1]
        if their_hand == LHS_PAPER[0]:
            return LOSE + RHS_ROCK[1]
        if their_hand == LHS_ROCK[0]:
            return DRAW + RHS_ROCK[1]

    if my_hand == RHS_PAPER[0]:
        if their_hand == LHS_ROCK[0]:
            return WIN + RHS_PAPER[1]
        if their_hand == LHS_SCISSORS[0]:
            return LOSE + RHS_PAPER[1]
        if their_hand == LHS_PAPER[0]:
            return DRAW + RHS_PAPER[1]

    if my_hand == RHS_SCISSORS[0]:
        if their_hand == LHS_PAPER[0]:
            return WIN + RHS_SCISSORS[1]
        if their_hand == LHS_ROCK[0]:
            return LOSE + RHS_SCISSORS[1]
        if their_hand == LHS_SCISSORS[0]:
            return DRAW + RHS_SCISSORS[1]


# Takes in opponents hand and desired outcome
# E.g. If their_hand is rock and desired outcome was a loss
#      then we would return scissors
def get_winning_hand(their_hand, desired_outcome):
    if desired_outcome == WIN_DESIRED:
        return WIN_LIST[their_hand]

    if desired_outcome == LOSE_DESIRED:
        return LOSE_LIST[their_hand]

    if desired_outcome == DRAW_DESIRED:
        return DRAW_LIST[their_hand]


def get_outcome_str(outcome):
    return DESIRED_OUTCOME[outcome]


def print_rounds(round_data):
    for curr_round in round_data:
        print(f"LHS plays %s" % curr_round[0], end=" |  ")
        print(f"RHS plays %s" % curr_round[1])
        print()


def print_rules():
    print("A = ROCK | B = PAPER | C = SCISSORS")
    print("ROCK beats SCISSORS | A ---> C")
    print("PAPER beats ROCK | B ---> A")
    print("SCISSORS beats PAPER | C ---> B")

    print("X = LOSE")
    print("Y = DRAW")
    print("Z = WIN")


def main():
    round_data = get_data("input.txt")

    total = 0
    for curr_round in round_data:
        total += did_you_win(curr_round[0], get_winning_hand(curr_round[0], curr_round[1]))

    print("Total:", total)


if __name__ == '__main__':
    main()
