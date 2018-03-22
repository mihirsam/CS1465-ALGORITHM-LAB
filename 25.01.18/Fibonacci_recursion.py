in1 = 0
in2 = 1
summ = 0
num = int(input("Enter the range : "))
print("%d\n%d" %(in1, in2))

def Fib(num, summ, in1, in2):
    if(summ < num):
        summ = in1 + in2
        in1 = in2
        in2 = summ
        print("{}" .format(summ))

        Fib(num, summ, in1, in2)

    else:
        print("\nExiting....")
        quit()

Fib(num, summ, in1, in2)
