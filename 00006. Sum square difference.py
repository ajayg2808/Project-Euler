#!/bin/python3
import math
import sys

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    sumOfSquares = (n * (n + 1) * (2 * n + 1)) / 6
    squareOfSum = (n * (n + 1) / 2) ** 2
    print(int(math.fabs(squareOfSum - sumOfSquares)))
