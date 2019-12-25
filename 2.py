from copy import deepcopy


def intcode_computer(input_list):
    read_head = 0
    while input_list[read_head] != 99:  # until end code found
        op_code = input_list[read_head]
        if op_code == 1 or op_code == 2:
            # Functions that take two inputs
            a = input_list[input_list[read_head + 1]]
            b = input_list[input_list[read_head + 2]]

            if op_code == 1:
                c = a + b
                # print("Adding {} and {} to get {}".format(a, b, c))
            elif op_code == 2:
                c = a * b
                # print("Multiplying {} and {} to get {}".format(a, b, c))
            input_list[input_list[read_head + 3]] = c

            # Move to next op code by moving forward 4 positions
            read_head += 4
        else:
            print(
                "Unknown Opcode {} at address {}, terminating".format(
                    input_list[read_head], read_head
                )
            )
            break
    return input_list


# a = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
# b = [1, 0, 0, 0, 99]
# c = [2, 3, 0, 3, 99]
# d = [2, 4, 4, 5, 99, 0]
# e = [1, 1, 1, 4, 99, 5, 6, 0, 99]
# print(a)
# print(intcode_computer(a))
# print(intcode_computer(b))
# print(intcode_computer(c))
# print(intcode_computer(d))
# print(intcode_computer(e))


puzzle = [
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    9,
    1,
    19,
    1,
    9,
    19,
    23,
    1,
    23,
    5,
    27,
    2,
    27,
    10,
    31,
    1,
    6,
    31,
    35,
    1,
    6,
    35,
    39,
    2,
    9,
    39,
    43,
    1,
    6,
    43,
    47,
    1,
    47,
    5,
    51,
    1,
    51,
    13,
    55,
    1,
    55,
    13,
    59,
    1,
    59,
    5,
    63,
    2,
    63,
    6,
    67,
    1,
    5,
    67,
    71,
    1,
    71,
    13,
    75,
    1,
    10,
    75,
    79,
    2,
    79,
    6,
    83,
    2,
    9,
    83,
    87,
    1,
    5,
    87,
    91,
    1,
    91,
    5,
    95,
    2,
    9,
    95,
    99,
    1,
    6,
    99,
    103,
    1,
    9,
    103,
    107,
    2,
    9,
    107,
    111,
    1,
    111,
    6,
    115,
    2,
    9,
    115,
    119,
    1,
    119,
    6,
    123,
    1,
    123,
    9,
    127,
    2,
    127,
    13,
    131,
    1,
    131,
    9,
    135,
    1,
    10,
    135,
    139,
    2,
    139,
    10,
    143,
    1,
    143,
    5,
    147,
    2,
    147,
    6,
    151,
    1,
    151,
    5,
    155,
    1,
    2,
    155,
    159,
    1,
    6,
    159,
    0,
    99,
    2,
    0,
    14,
    0,
]
puzz = deepcopy(puzzle)
puzz[1] = 12
puzz[2] = 2
print(intcode_computer(puzz)[0])


# Part 2
print("Starting part 2")
result = 19690720

a = 0
b = 0
while a < 100 and b < 100:
    puzz = deepcopy(puzzle)
    puzz[1] = a
    puzz[2] = b
    output = intcode_computer(puzz)
    if output[0] == result:
        print("noun = {}, verb = {}".format(a, b))
        print("Answer = {}".format(100 * a + b))
        break
    else:
        a += 1
        if a == 100:
            b += 1
            a = 0
