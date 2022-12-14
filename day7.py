#!/usr/bin/env python3

import json

from utils import get_input_list

home_dir = '/'

total = 0
max_size = 100000

total_fs = 70000000
unused = 30000000


def build_file_tree(command_list):
    filesystem = {home_dir: {}}

    current_dir = [home_dir]
    cdir = None
    for c in command_list:
        tokens = c.split(" ")
        if tokens[0] == '$':
            # Command
            if tokens[1] == 'ls':
                cdir = filesystem[home_dir]
                for d in current_dir[1:]:
                    cdir = cdir[d]
            if tokens[1] == 'cd':
                if tokens[2] == '..':
                    current_dir.pop()
                elif tokens[2] == home_dir:
                    current_dir = [home_dir]
                else:
                    current_dir.append(tokens[2])
        elif tokens[0] == 'dir':
            cdir[tokens[1]] = {}
        elif tokens[0].isdigit():
            cdir[tokens[1]] = int(tokens[0])

    return filesystem


def get_dir_sizes(dir_dict):
    size = 0
    for k, v in dir_dict.items():
        if isinstance(v, int) and k != 'size':
            size += v
        elif isinstance(v, dict):
            size += get_dir_sizes(v)
    dir_dict['size'] = size
    return size


def add_small_dirs(dir_dict):
    global total
    if dir_dict['size'] <= max_size:
        total += dir_dict['size']
    for v in dir_dict.values():
        if isinstance(v, dict):
            add_small_dirs(v)


def get_min_size(dir_dict):
    global min_size
    global min_del

    csize = dir_dict['size']

    if min_del <= csize < min_size:
        min_size = csize

    for v in dir_dict.values():
        if isinstance(v, dict):
            get_min_size(v)


if __name__ == "__main__":
    input_list = get_input_list(7)
    fs = build_file_tree(input_list)
    # with open('fs.json', 'w') as f:
    #     json.dump(fs, f, indent=4)

    __ = get_dir_sizes(fs['/'])
    # with open('fs-size.json', 'w') as f:
    #     json.dump(fs, f, indent=4)

    # total_size = add_small_dirs(fs['/'], [])
    add_small_dirs(fs['/'])
    print(f"1517599 total size of small dirs: {total}")

    free = total_fs - fs[home_dir]['size']
    min_del = unused - free
    min_size = fs['/']['size']
    print(min_del)

    get_min_size(fs['/'])
    print(f"part 2: min to delete is {min_size} and min to delete is {min_del}")




