num = int(input("Enter a number : "))

for i in range(1,num+1):
    j = 1
    while(j <= i):
        print(i, end = "")
        j += 1
    print("\n")
