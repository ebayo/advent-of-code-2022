#!/usr/bin/env python3
import string

from utils import get_input_list

priorities = '0' + string.ascii_lowercase + string.ascii_uppercase


def part1(rucksacks):
    misplaced_priorities = 0
    for rs in rucksacks:
        half_point = int(len(rs) / 2)
        for item in rs[:half_point]:
            if item in rs[half_point:]:
                misplaced_priorities += priorities.index(item)
                break
    return misplaced_priorities


def part2(rucksacks):
    if rucksacks[-1] == "":
        rucksacks = rucksacks[:-1]

    badge_priorities = 0
    for i in range(0, len(rucksacks), 3):
        first = set(rucksacks[i])
        second = set(rucksacks[i+1])
        third = set(rucksacks[i+2])

        for item in first:
            if item in second and item in third:
                badge_priorities += priorities.index(item)
                break

    return badge_priorities


if __name__ == "__main__":
    input_val = get_input_list(3)

    part1_priorities = part1(input_val)
    print(f"Part 1 solution is: {part1_priorities}")

    part2_priorities = part2(input_val)
    print(f"Part 2 solution is: {part2_priorities}")

