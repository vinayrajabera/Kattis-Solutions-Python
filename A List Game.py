#Trevor Little

import sys, math, functools, time

x= int(input())

score=0

increment= 1

while increment * increment <= x:
    if x % increment ==0:
        x= x/increment
        score+=1
        increment= 1
    if(x==1):
        score+=1
    increment+= 1
        
print(score)



