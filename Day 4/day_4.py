
def get_and_parse_data(filename: str):
    with open(filename, 'r') as fr:
        data = fr.readlines()
        ret_lines = []
        for line in data:
            split_line = line.strip().split(",")
            parsed_lines = []
            for sl in split_line:
                split_sl = sl.split("-")
                for i in range(len(split_sl)):
                    split_sl[i] = int(split_sl[i])
                parsed_lines.append(split_sl)
            ret_lines.append(parsed_lines)
    return ret_lines


def main():
    rounds = get_and_parse_data("input1.txt")

    # curr_round[0][0] = StartA
    # curr_round[0][1] = EndA
    # curr_round[1][0] = StartB
    # curr_round[1][1] = EndB

    count = 0
    for curr_round in rounds:
        # StartA <= EndB and StartB <= EndA
        if curr_round[0][0] <= curr_round[1][1] and curr_round[1][0] <= curr_round[0][1]:
            count += 1

    print(count)

    # count = 0
    # for curr_round in rounds:
    #     if curr_round[0][0] <= curr_round[1][0] and curr_round[0][1] >= curr_round[1][1]:
    #         # print(f"Rounds [{curr_round[0][0]} to {curr_round[0][1]}] encompasses rounds [{curr_round[1][0]} to {curr_round[1][1]}].")
    #         count += 1
    #     elif curr_round[1][0] <= curr_round[0][0] and curr_round[1][1] >= curr_round[0][1]:
    #         # print(f"Rounds [{curr_round[1][0]} to {curr_round[1][1]}] encompasses rounds [{curr_round[0][0]} to {curr_round[0][1]}].")
    #         count += 1
    # print(count)




if __name__ == '__main__':
    main()