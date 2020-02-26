def recursiveLinearSearch(arr, ele, i):
    if i == len(arr):
        print("Element not found")
        return

    if arr[i] == ele:
        print("Element found at " + i)
        return
    else:
        recursiveLinearSearch(arr, ele, i+1)

arr = list(map(int, input().split()))
ele = int(input())

recursiveLinearSearch(arr, ele, 0)
