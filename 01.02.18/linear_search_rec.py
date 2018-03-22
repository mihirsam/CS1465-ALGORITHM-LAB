import random
import sys
#sys.setrecursionlimit(100000)

def insert():
    ran = int(input("Enter the input size : "))
    return ran

def rand(num):
    for i in range(num):
        list.append(random.randrange(0,100000,1))

def search(ran, num, flag):
    while(flag <= ran-1):
        if(list[flag] == num):
            final.append(flag)
            flag += 1
            search(ran, num, flag)
        else:
            flag += 1
            search(ran, num, flag)

def res(num):
    if(len(final) == 0):
        print ("%d Not Found\n" %(num))
    else:
        print ("%d Found in : " %(num))
        for i in range(len(final)):
            print("list [%d] : " %(final[i]), end = "")
            print(list[final[i]])
        print("\n")
def disp():
    print("list : ", list)

def inp():
    num = int(input("Enter the number to search : "))
    return num

def exit():
    quit()

list = []
final = []
flag = 0
flag1 = 0
ran = 0

while(True):
    print("\n1.Insert\n2.Display\n3.Search\n4.Exit\n")
    choice = int(input("Enter your choice : "))

    if(choice == 1):
        print("1.Append Insert\n2.Truncate Insert\n")
        choice1 = int(input("Enter your choice : "))

        if(choice1 == 1):
            n = insert()
            ran = ran + n
            rand(ran)
            flag += 1
        elif(choice1 == 2):
            if(flag == 0):
                ran = ran + insert()
                rand(ran)
            else:
                del list
                del final
                list = []
                final = []
                ran = 0
                n = insert()
                ran = ran + n
                rand(ran)
        else:
            print("Invalid Input\n")
    elif(choice == 2):
        disp()
    elif(choice == 3):
        num = inp()
        flag1 = 0
        search(ran, num, flag1)
        res(num)
        del final
        final = []
    elif(choice == 4):
        exit()
    else:
        print("Invalid Input\n")
