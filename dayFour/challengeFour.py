import numpy as np




def sign(num):
    return -1 if num < 0 else 1


#TODO: Use case wise to just check all 8 directions or chcek each one?
#TODO: How to commit to a direction after deciding first letter? 

#TODO: Could've made a dictionary of all 8 directions each with related xDiff and yDiff instead of case

def partOne():
    wordSearch = np.zeros(0)
    totalVal = 0
    dirList = {"Up", "Up-Right", "Right", "Down-Right", "Down", "Down-Left", "Left", "Up-Left"}
    with open("dayfour\challengeFourInput.txt", 'r') as inputFile:
        for line in inputFile:
            wordSearch = np.append(wordSearch, line.rstrip())    #Create 2D array of lines

    # print(range()[0])
    # print(wordSearch)

    for currentRowInd in range(len(wordSearch)):
        for currentColInd in range(len(wordSearch[0])): #Square array
            if wordSearch[currentRowInd][currentColInd] == 'X': #Check if should even start
                print("Found X")
                for currDir in dirList:
                    match currDir: #TODO: add switch statement for dirs
                        case "Down":
                            xDiff = 0
                            yDiff = 4
                        case "Down-Right":
                            xDiff = 4
                            yDiff = 4
                        case "Right":
                            xDiff = 4
                            yDiff = 0
                        case "Up-Right":
                            xDiff = 4
                            yDiff = -4
                        case "Up":
                            xDiff = 0
                            yDiff = -4
                        case "Up-Left":
                            xDiff = -4
                            yDiff = -4
                        case "Left":
                            xDiff = -4
                            yDiff = 0
                        case "Down-Left":
                            xDiff = -4
                            yDiff = 4
                    if(xDiff == 0):
                        xArr = np.zeros(4)
                    else:
                        xArr = range(0, xDiff, sign(xDiff))
                    if(yDiff == 0):
                        yArr = np.zeros(4)
                    else:
                        yArr = range(0, yDiff, sign(yDiff))
                    #Check if the word would fit in the space
                    if(currentRowInd + yArr[-1] >= 0 and currentRowInd+yArr[-1] < len(wordSearch[0]) and currentColInd +xArr[-1] >= 0 and currentColInd+xArr[-1] < len(wordSearch)): #Make sure the next letter is in range
                        #Create The word (python does this well :3)
                        foundWord = wordSearch[currentRowInd + int(yArr[0])][currentColInd + int(xArr[0])] + wordSearch[currentRowInd + int(yArr[1])][currentColInd + int(xArr[1])] + wordSearch[currentRowInd + int(yArr[2])][currentColInd + int(xArr[2])] + wordSearch[currentRowInd + int(yArr[3])][currentColInd + int(xArr[3])]
                        print(foundWord, currDir)
                        # Check if word is "XMAS"
                        if(foundWord == "XMAS"):
                            totalVal += 1
                            print(currentColInd, currentRowInd)
    print(totalVal)
    # print(len(wordSearch))
    




def partTwo():
    wordSearch = np.zeros(0)
    totalVal = 0
    dirList = {"Up", "Up-Right", "Right", "Down-Right", "Down", "Down-Left", "Left", "Up-Left"}
    with open("dayfour\challengeFourTestData.txt", 'r') as inputFile:
        for line in inputFile:
            wordSearch = np.append(wordSearch, line.rstrip())    #Create 2D array of lines

    # print(range()[0])
    # print(wordSearch)

    for currentRowInd in range(len(wordSearch)):
        for currentColInd in range(len(wordSearch[0])): #Square array
            if wordSearch[currentRowInd][currentColInd] == 'M' or wordSearch[currentRowInd][currentColInd] == 'S': #Check if should even start
                if(currentRowInd+2 < len(wordSearch) and currentColInd+2 < len(wordSearch[0])): #Make sure the next letter is in range
                    firstDiagonal = wordSearch[currentRowInd][currentColInd] + wordSearch[currentRowInd+1][currentColInd+1] + wordSearch[currentRowInd+2][currentColInd+2]
                    secondDiagonal = wordSearch[currentRowInd][currentColInd+2] + wordSearch[currentRowInd+1][currentColInd+1] + wordSearch[currentRowInd+2][currentColInd]
                    if((firstDiagonal == "MAS" or firstDiagonal[::-1] == "MAS") and (secondDiagonal == "MAS" or secondDiagonal[::-1] == "MAS")):
                        totalVal += 1
    print(totalVal)

partTwo()