def partition(arr, lo, high):
    i = (lo-1)
    pivot = arr[high]

    for j in range(lo, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, lo, high):
    if lo < high:
        pi = partition(arr, lo, high)
        quickSort(arr, lo, pi-1)
        quickSort(arr, pi+1, high)


arr = [int(i) for i in input("").split()]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is: ", end="")
print(arr)
