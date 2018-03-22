import random
list = []

#for i in range(10):
#    x = random.randrange(1,10000,1)
#    list.append(x)

list = [int(x) for x in input("Enter the elements : ").split()]

print("List : ", list)
Max1 = 0
Max2 = 0
Min = list[0]

for i in range(len(list)):
    if(list[i] > Max2 and list[i] != Max1):
        if(list[i] > Max1):
            Max2 = Max1
            Max1 = list[i]
        else:
            Max2 = list[i]

    elif(list[i] < Min):
        Min = list[i]

    else:
        #nothing
        Max1 = Max1

#print("Maximum = {}\nSecond Max = {1}\nMin = {2}\n" .format(Max1, Max2,  Min))
print ("Max = %d\nSecond Max = %d\nMin = %d" %(Max1,  Max2, Min))
average = (Max1 + Max2)
average = average  / 2
print("Average of Max1 and Max2 is %d\n" %(average))
