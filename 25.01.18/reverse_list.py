list = [int(x) for x in input("Enter the elements for list: ").split()]
print ("Default list : ", list)

print("Reversed list  : [", end ="")
for i in range(len(list) -1, -1, -1):
    print(list[i], end = ", ")
print("]")
