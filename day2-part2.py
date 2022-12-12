#!/usr/bin/env python3

input_file = "inputs/day2-input.txt"

result_points = {"LOSE": 0, "DRAW": 3, "WIN": 6}
oponent_dict = {"A": 1, "B": 2, "C": 3}
part2_dict = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}


def myself(other, result):
    if result == "DRAW":
        return other
    if result == "LOSE":
        # Move to range 0-2 --> 1, -1 for the losing, %3 to come back to 0-2, +1 to move back to 1-3
        # (other - 1 - 1) % 3 + 1
        me = (other - 2) % 3 + 1
        return me
    if result == "WIN":
        # Same as with lose, but second operation is instead +1 and deletes first one
        # (other -1 + 1) % 3 + 1
        me = other % 3 + 1
        return me


def part2(input_list):
    points = 0
    for ot, res in input_list:
        points += result_points[res] + myself(ot, res)
    return points


if __name__ == "__main__":
    with open(input_file, 'r') as f:
        input_val = f.readlines()

    input_val = [v.strip() for v in input_val]      # Remove new line characters
    input_val = [v.split(" ") for v in input_val]   # Split between the two plays
    # print(input_val[0])
    input_val = [[oponent_dict[o], part2_dict[s]] for o, s in input_val]
    # print(input_val[0])
    part2_points = part2(input_val)
    print(f"Points obtained in part 2: {part2_points}")
