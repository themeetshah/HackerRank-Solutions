#!/bin/python3

import sys

t = int(input().strip())
give_sum = lambda n: lambda m: m * ((n - 1) // m) * ((n - 1) // m + 1) // 2
for a0 in range(t):
    n = int(input().strip())
    gs = give_sum(n)
    print(gs(3) + gs(5) - gs(15))
