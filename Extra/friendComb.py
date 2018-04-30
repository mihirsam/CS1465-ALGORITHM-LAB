num = int(input("Enter The Number Of Friends : "))
friendsList = []
flag = 0

for i in range(num):
    friendsList.append(i);

while(flag <= num):
    for i in range(num):
        for j in range(flag, i+1):
            print(friendsList[j])
        print("\n")
    flag += 1
