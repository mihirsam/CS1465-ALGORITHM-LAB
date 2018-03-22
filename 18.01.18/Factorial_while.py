# Factorial using while loop

num = int(input("Enter a number : "))

result = 1
while(num != 0):
    result = result * num
    num-= 1

print (result)
