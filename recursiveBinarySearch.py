def recursiveBinarySearch(arr, ele, high, low):
    if low > high:
        print("Element not found")
        return

    mid = (high + low) // 2
    
    if arr[mid] == ele:
        print("Element found at " + str(mid))
        return
    elif arr[mid] > ele:
        high = mid - 1
    else:
        low = mid + 1

    recursiveBinarySearch(arr, ele, high, low)
    
arr = list(map(int, input().split()))
ele = int(input())
recursiveBinarySearch(arr, ele, len(arr)-1, 0)
