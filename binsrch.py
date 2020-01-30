def binsrch(arr, low, high, key):
    if high>=low:
        mid = int(low + (high - low)/2)
        if arr[mid] == key:
            return 1
        elif arr[mid] > key:
            return binsrch(arr, low, mid-1, key)
        elif arr[mid] < key:
            return binsrch(arr, mid+1, high, key)
    else:
        return -1
tc = int(input("Enter number of testcases : "))
for _ in range(0, tc):
    length, key = list(map(int,input("").strip().split()))
    values = list(map(int,input("").strip().split()))[:length]
    print(binsrch(values, 0, (length-1), key))
