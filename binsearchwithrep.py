def binsrchrep(arr, key):
    low = 0
    rear = len(arr)-1
    while(low <= rear):
        mid = int((low+rear)/2)
        if(arr[mid] == key):
            #Found
            count = 0
            i = mid
            foundlow = False
            while(not foundlow):
                if(i>0):
                    if(arr[(i-1)] == key):
                        i = i-1
                    else:
                        foundlow = True
                else:
                    foundlow = True
            while(arr[i] == key and i<=rear):
                count += 1
                i += 1

            return count
        elif(arr[mid] > key):
            rear = mid
            continue
        elif(arr[mid] < key):
            low = mid+1
            continue
    return -1

arr =list(map(int, input("Enter array : ").split(" ")))
key = int(input("Enter key : "))
c = binsrchrep(arr, key)
if(c == -1):
    print("Not Found")
else:
    print("Found element. Count is " + str(c))

