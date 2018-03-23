import random
import time
def insertion_sort(ran):
    for i in range(2, ran):
        key = list[i]
        j = i - 1

        while(j>0 and list[j] > key):
            list[j+1] = list[j]
            j = j - 1

        list[j+1] = key


def input1(num):
    for i in range(0,num):
        list.append(random.randrange(0,10000,1))

def input2(num):
    for i in range(num-1, -1, -1):
        list.append(i)

def input3(num):
    for i in range(0,num):
        list.append(i)


index = [10, 100, 500, 10000, 20000, 50000]
list = []

for i in index:
    print("\n\nFor Index : {}\n" .format(i))
    #best case
    input3(i)
    start = time .time()
    insertion_sort(i)
    end = time.time()
    print("Best Case : {}\n" .format((end-start) * 1000))
    del list
    list = []

    #average
    input1(i)
    start = time .time()
    insertion_sort(i)
    end = time.time()
    print("Average Case : {}\n" .format((end-start) * 1000))
    del list
    list = []

    #worst
    input2(i)
    start = time .time()
    insertion_sort(i)
    end = time.time()
    print("Worst Case : {}\n" .format((end-start) * 1000))
    del list
    list = []
