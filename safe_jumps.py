def generateFib(n):
    first, second, third = 0, 1, 1
    list1 = []
    while third <= n + 1:
        list1.append(third)
        first, second = second, third
        third = first + second
    return list1


arr = [int(i) for i in input("Enter the safe/unsafe array : ").split()]
n = len(arr)
fibs = generateFib(n)

jumps = [n] * (n + 1)
arr += [1]
for i in range(n + 1):
    if arr[i] == 1:
        for fib in fibs:
            if i - fib == -1:
                jumps[i] = 1
            elif i - fib > -1:
                jumps[i] = min(jumps[i], jumps[i - fib] + 1)
print("Jumps taken: " + str(jumps[n]))
