#!/bin/python3

import sys


def smallest_multiple(a, b):
    n = a if a > b else b
    m = n
    value = a if a != n else b
    while n % value != 0:
        n += m
    return n


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    o = 1
    for i in range(2, n + 1):
        o = smallest_multiple(o, i)
    print(o)
