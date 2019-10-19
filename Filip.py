#Trevor Little

import sys


ip1, ip2= sys.stdin.readline().split()

newIp1= ip1[::-1]
newIp2= ip2[::-1]


    

if newIp1 > newIp2:
    print(newIp1)
else:
    print(newIp2)


