import numpy as np


def checkCompliance(currentManual, rules):
    for pgNumInd in range(len(currentManual)):
        for currentRule in rules:
            # print(currentRule.split("|")[0])
            # print(currentRule.split("|"))
            if currentManual[pgNumInd] in currentRule.split("|")[0]:
                foundIndex = list(currentManual).index(currentRule.split("|")[1]) if currentRule.split("|")[1] in list(currentManual) else -1
                if(foundIndex < pgNumInd and foundIndex != -1):
                    return False
    return True


def partOne():
    order = np.zeros(0)
    rules = np.zeros(0)
    ruleMode = True
    totalVal = 0
    with open("dayFive\challengeFiveTestData.txt", 'r') as inputFile:
        for line in inputFile:
            if(line.rstrip() == ""):
                ruleMode = False
            if (ruleMode):
                rules = np.append(rules, line.rstrip())
            else:
                order = np.append(order, line.rstrip())

    #.split(|) <-- TODO: use for rules to split what is important
    for currentManual in order:
        # return
        print(currentManual)
        if(checkCompliance(currentManual, rules)):
            totalVal += int(currentManual[int((len(currentManual) - 1)/2)])
            print(totalVal)
    print(totalVal)
    
                    
                    


partOne()