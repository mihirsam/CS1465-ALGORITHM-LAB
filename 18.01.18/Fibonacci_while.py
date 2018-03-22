# Fibonacci series using while loop

num = int(input("Enter a number here : "))
result = 1
in1 = 0
in2 = 1

while (result <= num):
    result = in1 + in2
    in1 = in2
    in2 = result

    if(result <= num):
        print (result)
    else:
        break
