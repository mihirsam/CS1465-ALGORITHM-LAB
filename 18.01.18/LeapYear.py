#  check for leap year
year = int(input("Enter the year :  "))

if(year % 100 == 0):
    if(year % 400 == 0):
        print("Leap year\n")

    else:
        print("Not a leap year\n")

elif(year % 4 == 0):
    print("Leap year\n")
else:
    print("Not a leap year\n")
