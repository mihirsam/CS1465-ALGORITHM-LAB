node = []
ratioList = []
graph = {}
finalResult = {}
totalProfit = 0

def fracKnap(graph, node, ratioList, capacity, totalProfit, finalResult):
    while(capacity != 0 and len(ratioList) != 0):
        #print(node)
        #print(graph)
        for i in node:
            if i in graph.keys():
                if(graph[i][2] == ratioList[0]):

                    if(graph[i][0] <= capacity):
                        capacity = capacity - graph[i][0]
                        totalProfit = totalProfit + graph[i][1]
                        finalResult[i] = 1
                        ratioList.pop(0)
                        del graph[i]

                        #print(capacity)
                        #print("Total Profit : {}" .format(totalProfit))

                        totalProfit = fracKnap(graph, node, ratioList, capacity, totalProfit, finalResult)

                    else:
                        totalProfit = totalProfit + ( (capacity/graph[i][0]) * (graph[i][1]) )
                        finalResult[i] = capacity/graph[i][0]
                        capacity = 0
                        ratioList.pop(0)
                        del graph[i]

                        #print(capacity)
                        #print("Total Profit : {}" .format(totalProfit))

                        totalProfit = fracKnap(graph, node, ratioList, capacity, totalProfit, finalResult)
                else:
                    pass
            else:
                pass

    return totalProfit


while(1):
    choice = int(input("\n\n1.Enter Value\n2.Exit\nChoice : "))

    if(choice == 1):
        tempList = []
        name = input("\n\nEnter The Name : ")
        weight = int(input("Enter Weight : "))
        profit = int(input("Enter Profit : "))
        ratio = profit/weight

        node.append(name)
        ratioList.append(ratio)
        tempList.append(weight)
        tempList.append(profit)
        tempList.append(ratio)

        graph[name] = tempList
        del tempList
    else:
        capacity = int(input("\nEnter The Total Capacity : "))
        break


for i in node:
    finalResult[i] = 0

ratioList.sort(reverse=True)
totalProfit = fracKnap(graph, node, ratioList, capacity, totalProfit, finalResult)

print("\n\n")
for i in node:
    print("{0} = {1}" .format(i, finalResult[i]))

print("Total Profit : {0}" .format(totalProfit))
#print("Total Profit : {}" .format(totalProfit))
