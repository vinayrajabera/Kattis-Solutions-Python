#Trevor Little

import sys

ip= str(sys.stdin.readline())

boolean= False

for i in range(len(ip)):
    if(ip[i]== 's' and ip[i+1]== 's'):
        boolean= True

if(boolean== True):
    print('hiss')
else:
    print('no hiss')
