#Trevor Little

import sys

while True:
    hour, minute= map(int, sys.stdin.readline().split())


    newMinute= minute - 45


    if newMinute < 0:
        hour-=1
        
    print(hour%24, newMinute%60)


    
