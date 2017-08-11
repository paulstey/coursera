#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from collections import namedtuple



Item = namedtuple("Item", ['index', 'value', 'weight'])

# def parse_input_data(input_data):
#     # parse the input
#     lines = input_data.split('\n')
#
#     first_line = lines[0].split()
#     item_count = int(first_line[0])
#     capacity = int(first_line[1])
#
#     items = []
#
#     # iterate through lines and append named tuples to
#     # the list `items`
#     for i in range(1, item_count+1):
#         line = lines[i]
#         parts = line.split()
#         items.append(Item(i-1, int(parts[0]), int(parts[1])))
#
#     return (items, capacity)

def build_table(items, capacity):
    p = len(items) + 1
    n = capacity + 1
    tbl = np.zeros((n, p), int)
    for j in range(1, p):
        for i in range(n):
            # previous column is all zero to this point
            if tbl[i, j-1] == 0:
                if items[j-1].weight <= i:
                    tbl[i, j] = items[j-1].value
            # value in previous column is non-zero
            elif tbl[i, j-1] > 0:
                if items[j-1].weight <= i:
                    remains_capacity = i - items[j-1].weight
                    if (items[j-1].value + tbl[remains_capacity, j-1]) > tbl[i, j-1]:
                        tbl[i, j] = items[j-1].value + tbl[remains_capacity, j-1]
                    elif items[j-1].value >= tbl[i, j-1]:
                        tbl[i, j] = items[j-1].value
                    else:
                        tbl[i, j] = tbl[i, j-1]
                else:
                    tbl[i, j] = tbl[i, j-1]
    return tbl


# def trace_back(tbl):
#     n, p = tbl.shape
#     i, j = n-1, p-1
#     keep_col = np.zeros(p, int)
#
#     while j > 0 and i > 0:
#         if tbl[i, j] != tbl[i, j-1]:
#             keep_col[j] = 1
#             i, j = i-1, j-1
#         else:
#             j -= 1
#     return keep_col[1:]




def prepare_output(value, taken):
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    item_count = int(first_line[0])
    capacity = int(first_line[1])

    items = []

    # iterate through lines and append named tuples to
    # the list `items`
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))


    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    tbl = build_table(items, capacity)
    n, p = tbl.shape
    i, j = n-1, p-1
    keep_col = np.zeros(p, int)

    while j > 0 and i > 0:
        if tbl[i, j] != tbl[i, j-1]:
            keep_col[j] = 1
            i, j = i-1, j-1
        else:
            j -= 1

    return prepare_output(tbl[-1][-1], keep_col[1:])



if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
