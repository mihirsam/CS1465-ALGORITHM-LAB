import time
import random

def selection_sort(ran):
   for i in range(ran-1,0,-1):
       key=0
       for j in range(1,i+1):
           if list[j]>list[key]:
               key = j

       temp = list[i]
       list[i] = list[key]
       list[key] = temp

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
    selection_sort(i)
    end = time.time()
    print("Best Case : {}\n" .format((end-start) * 1000))
    del list
    list = []

    #average
    input1(i)
    start = time .time()
    selection_sort(i)
    end = time.time()
    print("Average Case : {}\n" .format((end-start) * 1000))
    del list
    list = []

    #worst
    input2(i)
    start = time .time()
    selection_sort(i)
    end = time.time()
    print("Worst Case : {}\n" .format((end-start) * 1000))
    del list
    list = []
