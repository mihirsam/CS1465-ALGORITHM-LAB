import random
import time

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

def insert(x, num):
    for i in range(0,num):
        x.append(random.randrange(0,100000,1))


index = [1000, 5000, 10000, 20000, 25000, 50000, 100000, 1000000]
list1 = []

for i in index:
    print("\n\nFor Index : {}\n" .format(i))

    #average
    insert(list1, i)
    start = time .time()
    mergesort(list1)
    end = time.time()
    print("Average Case : {}\n" .format((end-start) * 1000))
    del list1
    list1 = []

    #best case
    insert(list1, i)
    list1.sort()
    start = time .time()
    mergesort(list1)
    end = time.time()
    print("Best Case : {}\n" .format((end-start) * 1000))
    del list1
    list1 = []



    #worst
    insert(list1, i)
    list1.reverse()
    start = time .time()
    mergesort(list1)
    end = time.time()
    print("Worst Case : {}\n" .format((end-start) * 1000))
    del list1
    list1 = []
