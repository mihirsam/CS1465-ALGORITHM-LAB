# to find the sum of numbers of an list using for loop

# list = int(input("How many numbers you want to input : "))
list = [int(x) for x in input("Put all the numbers : ").split()]
n = len(list)

sum = 0

print (list)
for i in range(len(list)):
	sum = sum + list[i]


print (sum)
