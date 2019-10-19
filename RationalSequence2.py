#Trevor Little

import sys, math, functools

def traversal(numerator, denominator):
    if numerator==1 and denominator==1:
        return 1
    elif numerator> denominator:
        return traversal(numerator, denominator - numerator)
        #return traversal(numerator*2, denominator)
    else numerator < denominator:
        return traversal(numerator - denominator), denominator)
        #return traversal(numerator *2, denominator +1) 
    


numOfCases= input()


for i in range(numOfCases):
    dataNumber, rational= input().split()
    numerator, denominator= map[int, numerator, denominator]
    

