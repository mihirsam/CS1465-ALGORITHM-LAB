import random
import time

def insert():
    ran = int(input("Enter the input size : "))
    return ran

def rand(num):
    for i in range(num):
        list.append(random.randrange(0,10000,1))

def l_search(ran, num):
    for i in range(ran):
        if(list[i] == num):
            final.append(i)
        else:
            pass

def b_search(ran, num):
    list.sort()
    low = 0
    high = ran-1
    flag = 0

    while(low <= high):

        mid = int((low+high)/2)

        if(list[mid] == num):
            print("\nFound in list[{}]" .format(mid))
            flag += 1
            break
        elif(list[mid] < num):
            low = mid+1
        elif(list[mid] > num):
            high = mid - 1
        else:
            pass
    if(flag==0):
        print("\nNOT FOUND!")
    else:
        pass

def b_search_time(ran, num):
    list.sort()
    low = 0
    high = ran-1

    while(low <= high):

        mid = int((low+high)/2)

        if(list[mid] == num):
            break
        elif(list[mid] < num):
            low = mid+1
        elif(list[mid] > num):
            high = mid - 1
        else:
            pass


def l_search_time(ran, num):
    for i in range(ran):
        if(list[i] == num):
            final.append(i)
            break;
        else:
            pass

def length():
    print("Length of List : {}\n" .format(len(list)));

def time_t(ran):
    if(ran == 0):
        print("\nLIST IS EMPTY!\n")
    else:
        print ("\n\nFOR INDEX : {}" .format(ran))
        print("\nLinear Search : ")
        start = time.time()
        l_search_time(ran, list[0])
        end = time.time()

        print ("\nBest Case : {} milli Seconds" .format((end-start)*1000))

        start = time.time()
        l_search_time(ran, 100000)
        end = time.time()

        print("Worst Case : {} milli Seconds" .format((end - start)*1000))

        print("\nBinary Search : ")
        list.sort()
        start = time.time()
        b_search_time(ran, int((ran-1)/2))
        end = time.time()

        print ("\nBest Case : {} milli Seconds" .format((end-start)*1000))

        start = time.time()
        l_search_time(ran, 100000)
        end = time.time()

        print("Worst Case : {} milli Seconds" .format((end - start)*1000))

def res(num):
    if(len(final) == 0):
        print ("\n%d Not Found\n" %(num))
    else:
        print ("\n%d Found in %d Indexes : " %(num, len(final)))
        for i in range(len(final)):
            print("list [%d] : " %(final[i]), end = "")
            print(list[final[i]])
        print("\nTotal : %d\n" %(len(final)))

def disp():
    print("\nFirst element  : ", list[len(list)-len(list)])
    print("Last element  : ", list[len(list) - 1])

def inp():
    num = int(input("Enter the number to search : "))
    return num

def exit():
    quit()

list = []
final = []
flag = 0
ran = 0

while(True):
    print("\n1.Insert\n2.Display\n3.Length\n4.Linear Search\n5.Binary Search\n6.Time Complexity\n7.Exit\n")
    choice = int(input("Enter your choice : "))

    if(choice == 1):
        print("1.Append Insert\n2.Truncate Insert\n")
        choice1 = int(input("Enter your choice : "))

        if(choice1 == 1):
            n = insert()
            ran = n
            rand(ran)
            flag += 1
        elif(choice1 == 2):
            """if(flag == 0):
                ran = ran + insert()
                rand(ran)
            else:"""
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
    elif(choice==3):
        length();
    elif(choice == 4):
        num = inp()
        l_search(ran,num)
        res(num)
        del final
        final = []
    elif(choice == 5):
        num = inp()
        b_search(ran, num)
    elif(choice == 6):
        time_t(ran)
        del final
        final = []
    elif(choice == 7):
        quit()
    else:
        print("Invalid Input\n")
