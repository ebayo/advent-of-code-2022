#!/usr/bin/env python3

input_file_template = "inputs/day{d}-input.txt"


def get_input_list(day_num):
    input_file = input_file_template.format(d=day_num)
    with open(input_file, 'r') as f:
        input_val = f.readlines()

    return [v.rstrip() for v in input_val]

