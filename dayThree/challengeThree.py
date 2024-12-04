import numpy as np
import re
# from sys import maxint

def checkMul(inputString, startVal):
    firstDigit = 0
    secondDigit = 0
    for firstNumOffset in range(1, 4):
        if(inputString[startVal:startVal+firstNumOffset].isdigit() and inputString[startVal+firstNumOffset] == ","):
            firstDigit = int(inputString[startVal:startVal+firstNumOffset])
            for secondNumOffset in range(1, 4):
                if(inputString[startVal+firstNumOffset+1:startVal+firstNumOffset+secondNumOffset+1].isdigit() and inputString[startVal+firstNumOffset+secondNumOffset+1]==")"): #TODO: need backslash?
                    secondDigit = int(inputString[startVal+firstNumOffset+1:startVal+firstNumOffset+secondNumOffset+1])
                    return (firstDigit*secondDigit)
    return 0
    

def partOne():
    inputString = ""
    totalVal = 0
    listOfDos = np.zeros(0)
    listOfDonts = np.zeros(0)
    with open("daythree\challengeThreeInput.txt", 'r') as inputFile:
        for line in inputFile:
            inputString += line
    
    for match in re.finditer("do()", inputString):
        print(match.end())
    for match in re.finditer("don't()", inputString):
        print(match.end())

    #TODO: if problem with white space, replace all whitespace with an invalid character
    for match in re.finditer("mul\(", inputString):
        tempMul = checkMul(inputString, match.end())
        totalVal += tempMul
    print(totalVal)

def checkIfDo(listOfDos, listOfDonts, mulVal):
    diffDos = [x - mulVal for x in listOfDos]
    diffDonts = [x - mulVal for x in listOfDonts]
    diffDosNeg = [i for i in diffDos if i < 0]
    diffDontsNeg = [i for i in diffDonts if i < 0]
    diffDosNeg = np.append(np.array(diffDosNeg), -2147483647)
    diffDontsNeg = np.append(np.array(diffDontsNeg), -2147483647)
    if(diffDosNeg.max() >= diffDontsNeg.max()): #if equal then both are max neg (nothing prior = do) if DosNegMax is greater than DontsNegMax then there was a Do more recently than a dont
        return True
    else:
        return False

def partTwo():
    inputString = ""
    totalVal = 0
    listOfDos = np.zeros(0)
    listOfDonts = np.zeros(0)
    with open("daythree\challengeThreeInput.txt", 'r') as inputFile:
        for line in inputFile:
            inputString += line
    
    for match in re.finditer("do()", inputString):
        listOfDos = np.append(listOfDos, match.end())
    for match in re.finditer("don't()", inputString):
        listOfDonts = np.append(listOfDonts, match.end())

    for match in re.finditer("mul\(", inputString):
        if(checkIfDo(listOfDos, listOfDonts, match.end())):
            tempMul = checkMul(inputString, match.end())
            totalVal += tempMul
    print(totalVal)
    


partTwo()