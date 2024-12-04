import numpy as np

def partOne():
    leftCol = np.zeros(1000)
    rightCol = np.zeros(1000)
    index = 0

    with open('challengeOneInput.txt', 'r') as inputFile:
        for line in inputFile:
            leftCol[index] = line.split()[0]
            rightCol[index] = line.split()[1]
            index += 1
    leftCol.sort()
    rightCol.sort()


    totalDifference = 0
    for i in range(len(leftCol)):
        currentDifference = abs(leftCol[i] - rightCol[i])
        totalDifference += currentDifference
    print(totalDifference)

def partTwo():
    leftCol = np.zeros(1000)
    rightCol = np.zeros(1000)
    index = 0

    with open('challengeOneInput.txt', 'r') as inputFile:
        for line in inputFile:
            leftCol[index] = line.split()[0]
            rightCol[index] = line.split()[1]
            index += 1
    leftCol.sort()
    rightCol.sort()

    totalDifference = 0
    for i in range(len(leftCol)):
        currentNumberOcc = (rightCol == leftCol[i]).sum()
        totalDifference += leftCol[i] * currentNumberOcc
    print(totalDifference)
    
partTwo()