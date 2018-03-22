# Fibonacci Series

in1 = 0
in2 = 1

num = int(input("Enter a number : "))

for i in range(1,num+1):

    new = in1 + in2
    if(new <= num):
        print (new)
        in1 = in2
        in2 = new
    else:
        break
