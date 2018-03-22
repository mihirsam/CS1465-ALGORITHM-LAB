n = int(input("Number of elements : "))
a = []
f = []
s =[]

for i in range(n):
    print("Activity  Selection : ")
    p = int(input("Start time : "))
    s.append(p)
    l = int(input("End time : "))
    f.append(l)

i =0
j =0

a.append(i+1)

for i in range(1,n):
    if(s[i] > f[j]):
        a.append(i+1)
        j = i

print("Selection task : ", a)
