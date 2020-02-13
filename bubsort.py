import random as rm
import time
def bubblesort(arr):
    len1 = len(arr)
    last = len1
    j = 0
    while(j < (last-1)):
        i = 0
        while(i < (last-1)):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        j += 1
    return arr

ranges = 10
while(ranges <= 10000):
    arr = (rm.randint(0, 200) for _ in range(0, ranges, 1))
    arr = list(arr)
    st1 = time.process_time()
    arr = bubblesort(arr)
    print("Time taken for " + str(ranges) + "numbers : " + str(time.process_time()-st1))
    ranges *= 10
