#Trevor Little

import sys, math, functools 

n= int(input())

for i in range(0,n):

    m= (input().split())
    print(m)
   
    smallestValue= m[0]
    if m[i] < smallestValue:
        smallestValue= m[i]
    print (i)
    
        

