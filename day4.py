#!/usr/bin/env python3

from utils import get_input_list


def AinB(a, b):
    amin, amax = a
    bmin, bmax = b

    if amin >= bmin and amax <= bmax:
        return True
    return False


def AoverB(a, b):
    amin, amax = a
    bmin, bmax = b

    # completly disjoited
    if bmax < amin or bmin > amax:
        return False
    return True


def part1(pair_list):
    num_pairs = 0
    for a, b in pair_list:
        if AinB(a, b) or AinB(b, a):
            num_pairs += 1
    return num_pairs


def part2(pair_list):
    num_pairs = 0
    for a, b in pair_list:
        if AoverB(a, b):
            num_pairs += 1
    return num_pairs


if __name__ == "__main__":
    input_val = get_input_list(4)

    if input_val[-1] == "":
        input_val = input_val[:-1]
    # print(input_val[0])
    input_val = [v.split(',') for v in input_val]
    input_val = [[a.split('-'), b.split('-')] for a, b in input_val]
    input_val = [[[int(a[0]), int(a[1])], [int(b[0]), int(b[1])]] for a, b in input_val]

    part1_pairs = part1(input_val)
    print(f"part 1: {part1_pairs}")

    part2_pairs = part2(input_val)
    print(f"part 1: {part2_pairs}")
