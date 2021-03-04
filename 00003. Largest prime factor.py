#!/bin/python3
import math
import sys

t = int(input().strip())


def maxPrimeFactor(n):
    maxPF = -1
    while n % 2 == 0:
        n >>= 1

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPF = i
            n = n / i

    if n > 2:
        maxPF = n

    return int(maxPF)


for _ in range(t):
    n = int(input().strip())
    print(maxPrimeFactor(n))
