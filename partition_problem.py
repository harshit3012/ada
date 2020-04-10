
def findPartition(arr, n):
    sum1 = 0
    i, j = 0, 0
    for i in range(n):
        sum1 += arr[i]
    if sum1 % 2 != 0:
        return False
    part = [[True for i in range(n + 1)]
            for j in range(sum1 // 2 + 1)]
    for i in range(0, n + 1):
        part[0][i] = True
    for i in range(1, sum1 // 2 + 1):
        part[i][0] = False
    for i in range(1, sum1 // 2 + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])
    return part[sum1 // 2][n]


arr = [int(x) for x in input("Enter array: ").split()]
n = len(arr)
if findPartition(arr, n):
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")
