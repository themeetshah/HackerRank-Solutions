#!/bin/python3

import sys
import math

def prime_factors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 2:
        factors.append(n)
    
    return factors

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    factors = prime_factors(n)
    print(max(factors))
