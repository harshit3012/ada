import time

def mergeArray(arr1, arr2):
    arr = []
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
        k += 1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
        k += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
        k += 1
    return arr

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    return mergeArray(mergeSort(arr[:mid]), mergeSort(arr[mid:]))


print("Enter the array : ", end="")
input_arr = [int(i) for i in input("").split(" ")]
start = time.time()
sorted_arr = mergeSort(input_arr)
end = time.time()
time_taken = end-start
print(f'Sorted Array: {sorted_arr} \nTime Taken: {time_taken}')
