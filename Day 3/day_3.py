import math
import numpy as np


def get_data(filename):
    with open(filename, 'r') as fr:
        return fr.readlines()


def list_to_dict(given_str: str):
    ret_dict = dict()

    for character in given_str:
        ret_dict[character] = False

    return ret_dict


def get_priority(character):
    val = ord(character)
    if 97 <= val <= 122:
        return val % 96
    elif 65 <= val <= 90:
        return val % 64 + 26


def get_rucksacks_p1(data):
    rucksacks = []
    for entry in data:
        list1 = list(entry.strip())
        middle_index = math.floor(len(list1) / 2)
        lhs = list1[0:middle_index]
        rhs = list1[middle_index:]
        rucksacks.append([list_to_dict(lhs), list_to_dict(rhs)])

    return rucksacks


def get_chunks(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


def get_rucksacks_p2(data):
    # Split into lists of 3
    rucksacks = list(get_chunks(data, 3))

    ret_rucksacks = []

    # Strip newlines
    for i in range(len(rucksacks)):
        rucksacks[i] = list(map(lambda x: x.strip(), rucksacks[i]))
        ret_rucksacks.append([list_to_dict(rucksacks[i][0]), list_to_dict(rucksacks[i][1]), list_to_dict(rucksacks[i][2])])

    return ret_rucksacks


def get_similarities_p1(lhs, rhs):
    similarities = []
    for key in lhs.keys():
        if key in rhs:
            rhs[key] = True

    for key in rhs.keys():
        if key in lhs:
            lhs[key] = True

    for key in lhs.keys():
        if lhs[key] is True:  # If rhs had a similarity in lhs
            if rhs[key] is True:  # If lhs had a similarity in rhs
                similarities.append(key)
    return similarities


def get_similarities_p2(lhs, mid, rhs):
    similarities = []

    for key in lhs.keys():
        if key in rhs:
            rhs[key] = True
        if key in mid:
            mid[key] = True

    for key in rhs.keys():
        if key in lhs:
            lhs[key] = True
        if key in mid:
            mid[key] = True

    for key in mid.keys():
        if key in lhs:
            lhs[key] = True
            if key in rhs:
                rhs[key] = True

    for key in lhs.keys():
        if lhs[key] is True:
            if key in rhs and rhs[key] is True:
                if key in mid and mid[key] is True:
                    similarities.append(key)

    return similarities


def main():
    data = get_data("input1.txt")
    rucksacks_p1 = get_rucksacks_p1(data)

    total1 = 0
    for rucksack in rucksacks_p1:
        similarities = get_similarities_p1(rucksack[0], rucksack[1])
        for similarity in similarities:
            total1 += get_priority(similarity)

    data = get_data("input2.txt")
    rucksacks_p2 = get_rucksacks_p2(data)

    similarities = []
    for rucksack in rucksacks_p2:
        similarities.append(get_similarities_p2(rucksack[0], rucksack[1], rucksack[2]))

    total2 = 0
    for similarity_lst in similarities:
        for similarity in similarity_lst:
            total2 += get_priority(similarity)

    print(total2)










if __name__ == '__main__':
    main()

