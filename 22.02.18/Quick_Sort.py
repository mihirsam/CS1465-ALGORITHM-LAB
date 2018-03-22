import random
import time
import sys

sys.setrecursionlimit(50000)

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

def insert(x, num):
    for i in range(0,num):
        x.append(random.randrange(0,100000,1))


index = [1000 , 5000, 10000, 20000, 25000]
list1 = []

for i in index:
    print("\n\nFor Index : {}\n" .format(i))

    #average
    insert(list1, i)
    start = time .time()
    quicksort(list1)
    end = time.time()
    print("Average Case : {}\n" .format((end-start) * 1000))

    #best case
    list1.reverse()
    start = time .time()
    quicksort(list1)
    end = time.time()
    print("Best Case : {}\n" .format((end-start) * 1000))

    #worst
    #list1.sort()
    #start = time .time()
    #quicksort(list1)
    #end = time.time()
    #print("Worst Case : {}\n" .format((end-start) * 1000))
    del list1
    list1 = []
