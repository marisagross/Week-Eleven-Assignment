# Basic Structure for a Random Walk simulation
# Dan Neumann
'''

You flip a coin.
If it comes up heads, you take a step forward;
tails means to take a step backward.
Repeat this n times.
Calculate distance from start

Repeat this process a large number of times.
Calculate and print the average for a given value of n
Start with 100 to 1000, step 10
'''

import random

# Define ranges here
startRange = 100
endRange = 1000
stepRange = 10 

def main():
    printHeader()
    for n in range(startRange,endRange,stepRange):
        averageDistance = getRandomWalk(n)
        print("For {} steps, the average distance is: {}".format(n,averageDistance))


def printHeader():
    print("The displacement: ")

def getRandomWalk(steps):
    # Calculate a random walk of given steps
    
    d = 0
    for toss in range(steps):
        coin = random.randint(0,1)
        if coin == 1:
            d = d + 1
        else:
            d = d - 1
            
    
    return d # replace with actual average

if __name__ == "__main__":
    main()