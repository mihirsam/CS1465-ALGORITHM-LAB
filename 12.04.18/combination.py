def takeInput():
    while(1):
        choice = int(input("1. Enter Number\n2. Enter Target\nChoice : "))

        if(choice == 1):
            value = int(input("Enter The Number : "));
            valuesList.append(value)

        elif(choice == 2):
            targetValue = int(input("Enter The Target Value : "))
            break

        else:
            print("Invalid Input")

    return valuesList, targetValue

def makeSet(valuesList, targetValue, count, targetList, tempIndex):

    if(sum(targetList) < targetValue):
        targetList.append(valuesList[count])
        count += 1
        makeSet(valuesList, targetValue, count, targetList, tempIndex)

    elif(sum(targetList) == targetValue):
        print(targetList, end = ' ')
        print(" = ", targetValue)
        targetList.append(valuesList[count])
        makeSet(valuesList, targetValue, count, targetList, tempIndex)

    elif(sum(targetList) > targetValue):
        delNode(valuesList, targetValue, count, targetList, tempIndex)
    else:
        pass


def delNode(valuesList, targetValue, count, targetList, tempIndex):
    targetList.pop(-1)

    for i in valuesList:
        if(targetList[-1] == i):
            tempIndex = valuesList.index(i)
        else:
            pass

    tempIndex += 1

    if(tempIndex > (len(valuesList) -1)):
        if(valuesList[len(valuesList)-1] == targetList[0]):
            return
        else:
            delNode(valuesList, targetValue, count, targetList, tempIndex)
    else:
        count = 0
        targetList.pop(-1)
        targetList.append(valuesList[tempIndex])
        makeSet(valuesList, targetValue, count, targetList, tempIndex)


count = 0
tempIndex = 0
valuesList = []
targetValue = []
targetList = []

valuesList, targetValue = takeInput()
valuesList.sort()
makeSet(valuesList, targetValue, count, targetList, tempIndex)
