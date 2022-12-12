#!/usr/bin/env python3

input_file = "inputs/day2-input.txt"

result_points = {"LOSE": 0, "DRAW": 3, "WIN": 6}
oponent_dict = {"A": 1, "B": 2, "C": 3}
part1_dict = {"X": 1, "Y": 2, "Z": 3}
part2_dict = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}


def game(other, myself):
    if other == myself:
        return result_points["DRAW"]
    if myself - other == 1:
        return result_points["WIN"]
    if myself - other % 3 == 1:
        return result_points["WIN"]
    return result_points["LOSE"]


def part1(input_list):
    points = 0
    for op, me in input_list:
        points += me + game(op, me)

    return points


if __name__ == "__main__":
    with open(input_file, 'r') as f:
        input_val = f.readlines()

    input_val = [v.strip() for v in input_val]      # Remove new line characters
    input_val = [v.split(" ") for v in input_val]   # Split between the two plays
    # print(input_val[0])
    input_val = [[oponent_dict[o], part1_dict[s]] for o, s in input_val]
    # print(input_val[0])
    part1_points = part1(input_val)
    print(f"Points obtained in part 1: {part1_points}")
