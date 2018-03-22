import random
import time

def rand(num):
    for i in range(num):
        list.append(random.randrange(0,10000,1))


def l_search_time(ran, num):
    for i in range(ran):
        if(list[i] == num):
            break;
        else:
            pass

def time_t(ran):
    if(ran == 0):
        print("\nLIST IS EMPTY!\n")
    else:
        print ("\n\nFOR INDEX : {}" .format(ran))
        print("\nLINEAR SEARCH : ")
        start = time.time()
        l_search_time(ran, list[0])
        end = time.time()

        print ("Best Case : {} milli Seconds" .format((end-start)*1000))

        start = time.time()
        l_search_time(ran, list[int((ran-1)/2)])
        end = time.time()

        print ("Average Case : {} milli Seconds" .format((end-start)*1000))

        start = time.time()
        l_search_time(ran, 100000)
        end = time.time()

        print("Worst Case : {} milli Seconds" .format((end - start)*1000))

list = []
inputs = [10, 100, 500, 10000, 20000, 50000, 100000, 150000, 500000, 1000000]

for i in inputs:
    del list
    list = []
    rand(i)
    time_t(i)
