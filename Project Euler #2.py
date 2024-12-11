#!/bin/python3

import sys

def gs(n):
    a=1
    b=2
    sum1=0
    while b<=n:
        if b%2==0 and b<n:
            sum1+=b
        a,b=b,a+b
    return sum1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(gs(n))
