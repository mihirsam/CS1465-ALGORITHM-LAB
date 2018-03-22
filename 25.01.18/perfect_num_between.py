# not working, yet!
def insert():
    num = int(input("Enter the range here : "))
    return num

def prime(num):
    flag = 0
    for i in range(2,num+1):
        for j in range(1,i+1):
            if(i % j == 0):
                list.append(i)
                flag += 1
            else:
                num = num
        check(i)
        del list[0:flag]
        flag = 0

def check(num):
    summ = 0
    for i in range(len(list)):
        summ = summ + list[i]

    if(summ / 2 == num):
        print("%d is a perfect NUmber \n" %(num))
    else:
        pass

def exit():
    quit()


while(True):
    print("1.Check\n2.Exit")
    choice = int(input("Enter your choice : "))

    if(choice == 1):
        list = []
        num = insert()
        prime(num)

    elif(choice == 2):
        exit()
    else:
        print("Invalid Input\n")
