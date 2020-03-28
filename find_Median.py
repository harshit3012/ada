def median1(arr1):
    if len(arr1) == 0:
        return 0
    if len(arr1) % 2 == 0:
        return (arr1[len(arr1)//2] + arr1[(len(arr1)//2)-1])/2
    else:
        return arr1[len(arr1)//2]


def findMedian(arr1, arr2):
    n = len(arr1)
    m = n // 2

    if not n:
        return -1
    elif n == 1:
        return (arr1[0] + arr2[0]) // 2
    elif n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) // 2
    else:
        m1, m2 = median1(arr1), median1(arr2)

        if m1 > m2:
            if n % 2 == 0:
                return findMedian(arr1[:m + 1], arr2[m - 1:])
            else:
                return findMedian(arr1[:m + 1], arr2[m:])
        else:
            if n % 2 == 0:
                return findMedian(arr2[:m + 1], arr1[m - 1:])
            else:
                return findMedian(arr2[:m + 1], arr1[m:])


print("Enter arr1: ", end="")
arr1 = [int(i) for i in input("").split()]
print("Enter arr2: ", end="")
arr2 = [int(i) for i in input("").split()]
print(findMedian(arr1, arr2))
