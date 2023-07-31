#!/usr/bin/env python3

def print_fibonacci(length):
    fibb_list = []
    for i in range(length):
        if i == 0 or i == 1:
            fibb_list.append(i)
        else:
            fibb_list.append(fibb_list[i-2] + fibb_list[i-1])
    print(fibb_list)