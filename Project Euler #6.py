#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum1=n*(n+1)//2
    sq_sum=sum1**2
    sum_sq=sum1*((2*n)+1)//3
    print(sq_sum-sum_sq)
