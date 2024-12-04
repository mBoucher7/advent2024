import numpy as np

def testLevel(level):
    diffValues = np.zeros(0)
    splitLevel = level.split()
    for index in range(len(splitLevel) - 1):
        diffValues = np.append(diffValues, int(splitLevel[index]) - int(splitLevel[index+1]))
    if(diffValues.max() > 0 and diffValues.min() < 0 or diffValues.max() > 3 or diffValues.min() < -3 or 0 in diffValues): #If increases and decreases in same level, or changes more than 3 or has a change of 0 --> Fail
        return False
    else:
        return True


def partOne():
    reports = np.zeros(0)
    passedReports = 0

    with open("daytwo\challengeTwoInput.txt", 'r') as inputFile:
        print("pass")
        for line in inputFile:
            reports = np.append(reports, line)
    totalReports = 0
    for level in reports:
        totalReports += 1
        if(testLevel(level)):
            passedReports += 1
        
    print(passedReports)

def testLevelTwo(level):
    splitLevel = level.split()
    for attemptNum in range(len(splitLevel)):
        diffValues = np.zeros(0)
        trimLevel = np.delete(splitLevel, attemptNum)
        for index in range(len(trimLevel) - 1):
            diffValues = np.append(diffValues, int(trimLevel[index]) - int(trimLevel[index+1]))
        if(not (diffValues.max() > 0 and diffValues.min() < 0 or diffValues.max() > 3 or diffValues.min() < -3 or 0 in diffValues)): #If increases and decreases in same level, or changes more than 3 or has a change of 0 --> Fail
            return True
        else:
            print("trimmed", trimLevel)
            print("diffed", diffValues)
    print(splitLevel)
    return False

def partTwo():
    reports = np.zeros(0)
    passedReports = 0
    with open("daytwo\challengeTwoInput.txt", 'r') as inputFile:
        print("pass")
        for line in inputFile:
            reports = np.append(reports, line)
    totalReports = 0
    for level in reports:
        totalReports += 1
        if(testLevelTwo(level)):
            passedReports += 1
    print(passedReports)


partTwo()