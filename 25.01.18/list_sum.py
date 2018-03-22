list = [int(x) for x in input("Enter the elements of the list : ").split()]
sum = 0
for i in range(len(list)):
    sum += list[i]

print ("Sum of elements of list : %d\n" %(sum))
