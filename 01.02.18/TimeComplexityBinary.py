import random
import time



def time_t(ran):
    if(ran == 0):
        print("\nLIST IS EMPTY!\n")
    else:
        print ("\n\nFOR INDEX : {}" .format(ran))

        print("\nBINARY SEARCH : ")
        list.sort()
        start = time.time()
        b_search_time(ran, int((ran-1)/2))
        end = time.time()

        print ("Best Case : {} milli Seconds" .format((end-start)*1000))

        start = time.time()
        b_search_time(ran, int((ran-1)/4))
        end = time.time()

        print ("Average Case : {} milli Seconds" .format((end-start)*1000))


        start = time.time()
        b_search_time(ran, list[ran-1])
        end = time.time()

        print("Worst Case : {} milli Seconds" .format((end - start)*1000))

def b_search_time(ran, num):
    list.sort()
    low = 0
    high = ran-1

    while(low <= high):

        mid = int((low+high)/2)

        if(list[mid] == num):
            break
        elif(list[mid] < num):
            low = mid+1
        elif(list[mid] > num):
            high = mid - 1
        else:
            pass

def rand(num):
    for i in range(num):
        list.append(random.randrange(0,10000,1))


list = []
inputs = [10, 100, 500, 10000, 20000, 50000, 100000, 150000, 500000, 1000000]

for i in inputs:
    del list
    list = []
    rand(i)
    time_t(i)
