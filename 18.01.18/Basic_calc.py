# basic calc

def add():
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))
    print ("Addition = %d\n" %(num1+num2))

def sub():
    num1 = int(input("Enter num1  : "))
    num2 = int(input("Enter num2 : "))
    print("Subtraction = %d\n" %(num1 - num2))

def mul():
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))
    print("Multiplication = %d\n" %(num1 * num2))

def div():
    num1 = int(input("Enter num1 : "))
    num1 = int(input("Enter num1 : "))
    print("Division = %d\n" %(num1/num2))


while(True):
    choice = int(input("1.Add\n2.Subtraction\n3.Multiply\n4.Divide\n5.Exit\nYour choice here : "))

    if(choice == 1):
        add()
    elif(choice == 2):
        sub()
    elif(choice == 3):
        mul()
    elif(choice == 4):
        div()
    elif(choice == 5):
        break
        quit()
    else:
        print ("Invalid input\n")
