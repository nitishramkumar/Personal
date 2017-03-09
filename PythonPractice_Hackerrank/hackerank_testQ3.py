import sys
import os
import math

def diceGame(N):
    expectedValues = []
    expectedValues.append(3.5)

    for count in range(1,N):
        previousExp = expectedValues[count-1]
        totalSum = 0
        totalSum += previousExp if previousExp > 1 else 1
        totalSum += previousExp if previousExp > 2 else 2
        totalSum += previousExp if previousExp > 3 else 3
        totalSum += previousExp if previousExp > 4 else 4
        totalSum += previousExp if previousExp > 5 else 5
        totalSum += previousExp if previousExp > 6 else 6

        expectedValues.append(totalSum/6)

    print(math.floor(float("%.2f"%(expectedValues[N-1])) * 10000))

script,N = sys.argv
diceGame(int(N))
