import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    res = []
    for i in range(100):
        if random.randint(0,1) == 0:
            res.append('H')
        else:
            res.append('T')
    
    prev = ''
    cur = 0
    for j in res:
        if j == prev:
            cur +=1
            
            if cur >= 6:
                numberOfStreaks += 1
        else:
            prev = j
            cur = 1

print(round(numberOfStreaks/(1000000),2))