#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n3 = (n - 1) // 3
    n5 = (n - 1) // 5
    n15 = (n - 1) // 15
    a = (n - 1) % 3
    a = n - 1 - a
    a = a // 3
    b = (n - 1) % 5
    b = n - 1 - b
    b = b // 5
    d = (n - 1) % 15
    d = n - 1 - d
    d = d // 15
    c = 3 * a * (a + 1) // 2 + 5 * b * (b + 1) // 2 - 15 * d * (d + 1) // 2
    print(int(c))
