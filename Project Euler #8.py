#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    
    max_pdt=0
    for i in range(n-k+1):
        nums=num[i:i+k]    
        prdt=1
        for j in nums:
            prdt*=int(j)
        max_pdt=max(max_pdt,prdt)
    print(max_pdt)
