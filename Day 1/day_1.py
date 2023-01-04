import numpy as np

def read_input(filename):
    with open(filename, 'r') as fr:
        data = fr.read()
        lines = data.split("\n")

    counter = 0     # Counter for appending to final
    final = [[]]    # List of lists, each containing elves intake
    for line in lines:
        if line == '':
            counter += 1
            final.append(list())
        else:
            final[counter].append(int(line))
    return final


def get_sum(elf):
    total = 0
    for item in elf:
        total += item
    return total


def get_sums_total(sums):
    total = 0
    for sum in sums:
        total += sum
    return total


def main():
    data = read_input("input.txt")
    print(mask)

    sums = []
    for elf in data:
        sums.append(get_sum(elf))

    sums.sort()
    print(get_sums_total(sums[len(sums)-3::]))
    return max


if __name__ == '__main__':
    main()
