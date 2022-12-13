#!/usr/bin/env python3

from utils import get_input_list


def initial_stacks(stack_list, num):
    stks = [[] for __ in range(num + 1)]
    for row in stack_list[::-1]:
        crates = [row[i:i+3] for i in range(0, len(row), 4)]
        for i, c in enumerate(crates):
            cc = c.strip()
            if cc != '':
                stks[i+1].append(cc[1])
    return stks


def get_instructions(instruction_list):
    ins = []
    for i in instruction_list:
        tokens = i.split(' ')
        ins.append([int(t) for t in tokens[1::2]])
    return ins


if __name__ == "__main__":
    input_val = get_input_list(5)

    break_line = 0
    for j, line in enumerate(input_val):
        if line == '':
            break_line = j
            break

    num_stacks = int(input_val[break_line - 1].strip()[-1])
    stacks = initial_stacks(input_val[:break_line - 1], num_stacks)
    instructions = get_instructions(input_val[break_line+1:])

    for num, src, dst in instructions:
        stacks[dst].extend(stacks[src][-num:])
        stacks[src] = stacks[src][:-num]

    for st in stacks:
        print(st)


    part2_word = [st[-1] for st in stacks[1:]]
    print(f"final state part2: {''.join(part2_word)}")

