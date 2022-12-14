#!/usr/bin/env python3

from utils import get_input_list

if __name__ == "__main__":
    input_datastream = get_input_list(6)[0]
    # print(input_datastream)

    num_chars = 14

    for i, v in enumerate(input_datastream):
        j = i+1
        if j < num_chars:
            continue
        if len(set(input_datastream[j-num_chars:j])) == num_chars:
            print(f"index : {j}, seq : {input_datastream[j-num_chars:j]}")
            break
