#!/bin/python3

import sys

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    f1 = 1
    f2 = 2
    f3 = 2
    if n < 5:
        print(2)
    else:
        sum = 0
        while f3 <= n:
            if f3 % 2 == 0:
                sum += f3
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        print(sum)