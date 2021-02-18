import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    coinFlips = []
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        if(random.randint(0,1) == 0):
            coinFlips.append('heads')
        else:
            coinFlips.append('tails')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for n in range(len(coinFlips) - 5):
        sub = coinFlips[n:(n + 6)]
        count = sub.count('heads')
        if(count == 6 or count == 0):
            numberOfStreaks += 1
            break
print('Chance of streak: %s%%' % (numberOfStreaks / 100))