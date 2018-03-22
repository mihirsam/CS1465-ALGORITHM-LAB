# printing elements of list in reverse order without inbuilt function

List = [int(x) for x  in input("Enter the list elements : ").split()]

for i in range(len(List) - 1, -1, -1):
    print(List[i])
