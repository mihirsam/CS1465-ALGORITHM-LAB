def insert():
    num = int(input("Enter the number here : "))
    return num

def prime(num):
    for i in range(1,num+1):
        if(num % i == 0):
            list.append(i)
        else:
            num = num

def check(num):
    summ = 0
    for i in range(len(list)):
        summ = summ + list[i]

    if(summ / 2 == num):
        print("%d is a perfect NUmber \n" %(num))
    else:
        print("%d is not a perfect number \n" %(num))

def exit():
    quit()


while(True):
    print("1.Check\n2.Exit")
    choice = int(input("Enter your choice : "))

    if(choice == 1):
        list = []
        num = insert()
        prime(num)
        check(num)
        del list

    elif(choice == 2):
        exit()
    else:
        print("Invalid Input\n")
