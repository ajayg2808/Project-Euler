#!/bin/python3

import sys
from functools import reduce
from operator import mul

t = int(input().strip())
for _ in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    num = num.replace(" ", "").replace("\n", "")
    digits = [int(ch) for ch in num]
    ans = 0
    for i in range(n - k + 1):
        sub = digits[i:i + k]
        product = reduce(mul, sub, 1)
        ans = max(ans, product)

    print(ans)
