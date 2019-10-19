#Trevor Little


import sys, math

numbers= []

for i in range(5):
    total= 0
    values= sys.stdin.readline().split()
    for j in values:
        total+= int(j)
    numbers.append(total)

participant= 0
m= 0

for k in range(5):
    if max(m, numbers[k])== numbers[k]:
        participant= k + 1
        m= numbers[k]


print(participant, m)
        
