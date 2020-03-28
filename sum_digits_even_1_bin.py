def count1(num):
    countOf1 = 0
    while(num):
        num = num & (num - 1)
        countOf1 += 1

    if (countOf1 % 2 == 0):
        return True
    else:
        return False


def sumOfDigits(n):
    sum1 = 0
    while (n != 0):
        sum1 += n % 10
        n //= 10

    return sum1


arr = [int(i) for i in input("Enter the array : ").split()]
n = len(arr)
total = 0
for i in range(n):
    if (count1(arr[i])):
        total += sumOfDigits(arr[i])
print(total)
