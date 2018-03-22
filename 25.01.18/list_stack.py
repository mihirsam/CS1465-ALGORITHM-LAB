import random
list = []
flag = 0

def append(flag):
    x = random.randrange(0,1000,1)
    list.append(x)
    flag += 1
    print("%d has been appended to the list" %(x))
    return flag

def display():
    print("List : ", list)

def length(flag):
    print("Length of the list : %d\n" %(flag))

def maxx(flag):
    Max = 0
    for i in range(flag):
        if(list[i] > Max):
            Max = list[i]
        else:
            Max = Max

    print("Largest number of list : %d \n" %(Max))

def minn(flag):
    Min = list[0]
    for i in range(flag):
        if(list[i] < Min):
            Min = list[i]
        else:
            Min = Min

    print  ("Smallest number in list : %d \n" %(Min))

def exit():
    print("Exiting ....")
    quit()

while(True):
    print("\n1.Append\n2.Display\n3.Length\n4.Maximum\n5.Minimum\n6.Exit\n")
    choice = int(input("Enter your choice : "))

    if(choice == 1):
        flag = append(flag)

    elif(choice == 2):
        display()

    elif(choice == 3):
        length(flag)

    elif(choice == 4):
        maxx(flag)

    elif(choice == 5):
        minn(flag)

    elif(choice == 6):
        exit()

    else:
        print ("Invalid  Input \n")
