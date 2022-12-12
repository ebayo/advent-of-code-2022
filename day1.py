#!/usr/bin/env python3

input_file = "inputs/day1-input.txt"


def part1(input_list):
    cal = 0
    mx_cal = 0
    for v in input_list:
        if v != "":
            cal += int(v)
            # print(cal)
        elif cal >= mx_cal:
            # print(cal)
            mx_cal = cal
            cal = 0
        else:
            # print(cal)
            cal = 0
    return mx_cal


def part2(input_list):
    cal = 0
    top3 = [0, 0, 0]
    for v in input_list:
        if v != "":
            cal += int(v)
        else:
            # Could be changed to work with indexes wth enumerate and using that for list indexing and displacement
            # --> for i, mx_v in enumerate(top)
            if cal >= top3[0]:
                top3[1:] = top3[:2]
                top3[0] = cal
            elif cal >= top3[1]:
                top3[2] = top3[1]
                top3[1] = cal
            elif cal >= top3[2]:
                top3[2] = cal
            cal = 0
    return sum(top3)


if __name__ == "__main__":
    with open(input_file, 'r') as f:
        input_val = f.readlines()
    # stripped_input = [v.strip() for v in input_val]
    # elfs_calories = []

    # New line character works as a signal to switch and compare elfs calorie values,
    # ensure last value on the list should be "\n"
    input_val = input_val + ["\n"] if input_val[-1] != "\n" else input_val
    input_val = [v.strip() for v in input_val]
    max_cal = part1(input_val)
    print(f"top1 elf carries : {max_cal}")

    max3_cal = part2(input_val)
    print(f"top3 elf carry : {max3_cal}")
