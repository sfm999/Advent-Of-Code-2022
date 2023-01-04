def explain_instruction(instruction):
    print(f"move %d from %d to %d" % (instruction[0], instruction[1], instruction[2]))


def gen_space_lst(n):
    list_of_spaces = [" "] * n
    return list_of_spaces


def get_and_parse_data(filename):

    with open(filename, 'r') as fr:
        data = fr.read()                        # Read in data
        end_of_cols = data.index('1')              # Find when instructions start
        start_of_instructions = data.index('move')              # Find when instructions start
        str_stacks = data[:end_of_cols-1]               # Split crates from instructions
        column_count = data[end_of_cols:start_of_instructions]
        instructions = data[start_of_instructions:]             # Split instructions from crates

    # Parse the column counts
    # Done before str_stacks due to using total_cols in str_stacks parsing
    col_count_lst = column_count.split()
    col_count_lst = list(map(lambda x: int(x), col_count_lst))
    total_cols = max(col_count_lst)



    # Parse the columns by keeping any spaces but stripping the square brackets
    # Then we pad out the list with spaces till its length is equivalent to total_cols
    # This allows us to identify which column each value belongs to as each row
    # will now be as long as the column count and will allow accurate allocation of crates to their stacks
    split_str_stacks = str_stacks.splitlines()              # Split the huge stack string by line
    temp_stacks = []                                       # Holds the parsed and padded lines
    for i in range(len(split_str_stacks)):
        tmp_lst = []
        for j in range(len(split_str_stacks[i])):
            # Each character, besides the first, has 3 characters between them and the next
            # Note the example you are to omit every first space.
            # E.g. [ A ]  [ B ] | { '[': 0, 'A': 1, ..., 'B': 5, ']': 6
            try:
                tmp_lst.append(split_str_stacks[i][1+4*j])
            except IndexError:
                continue
        temp_stacks.append(tmp_lst)

    # Generate the padding for each list, padding is a series of spaces
    # Each list will now be total_cols in length
    for i in range(len(temp_stacks)):
        curr_len = len(temp_stacks[i])
        if curr_len < total_cols:
            temp_stacks[i] += gen_space_lst(total_cols - curr_len)

    # Create crate_stacks, helps with later indexing
    crate_stacks = list()
    for i in range(total_cols):
        crate_stacks.append(list())

    # Parse crates from temp_stacks to crate_stack
    for row in temp_stacks:
        for i in range(len(row)):
            if row[i].isalpha():
                crate_stacks[i].append(row[i])

    for i in range(len(crate_stacks)):
        crate_stacks[i].reverse()

    # Parse the given instructions
    # These come in the form of 'Move X from Y to Z'
        # X corresponds to the amount to move
        # Y dictates to the stack to take from
        # Z indicates the stack to move them to
    # We want to strip it to a list in form of [X, Y, Z]
    instruction_lst = []
    for instruction in instructions.splitlines():   # Split the instructions from the string
        lst = []                                    # List that will hold each instruction sequence
        for inst in instruction:                    # Iterate split lines
            if inst.isnumeric():                    # Determine if curr char in line is numeric
                lst.append(int(inst))             # If so, add to lst
        instruction_lst.append(lst)                 # Add lst to instruction_lst

    return crate_stacks, instruction_lst        # Return the crate_stacks and the instruction list


# instruction[0] = QUANTITY to take
# instruction[1] = SOURCE to take from
# instruction[2] = DESTINATION to deliver to
def move_crate(crate_stacks, instruction):
    qty = instruction[0]
    src = instruction[1] - 1
    dst = instruction[2] - 1

    print("Instruction given:", instruction)

    print("Destination crate BEFORE move:", crate_stacks[dst])

    print("Source crate BEFORE move:", crate_stacks[src])
    print("Destination crate BEFORE move:", crate_stacks[dst])

    print("Crates to take from source crate:", crate_stacks[src][-qty:])

    temp_lst = crate_stacks[src][-qty:]
    temp_lst.reverse()
    crate_stacks[dst] += temp_lst

    print("Destination crate AFTER move:", crate_stacks[dst])

    crate_stacks[src] = crate_stacks[src][:-qty]

    print("Source crate AFTER move:", crate_stacks[src])

    print("Crates current state")
    print(crate_stacks)
    print("-----------------------------------------------\n\n")

    return crate_stacks


def get_topmost_crates(crate_stacks):
    topmost_crates = list()
    for stack in crate_stacks:
        if stack:
            topmost_crates.append(stack[-1])
    return topmost_crates


def main():
    crate_stacks, instructions = get_and_parse_data("input.txt")

    for instruction in instructions:
        move_crate(crate_stacks, instruction)

    print(get_topmost_crates(crate_stacks))


if __name__ == '__main__':
    main()