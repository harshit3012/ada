def countChange(coins, m, n):
    if (n == 0):
        return 1
    if (n < 0):
        return 0
    if (m <= 0 and n >= 1):
        return 0
    return countChange(coins, m - 1, n) + countChange(coins, m, n-coins[m-1])


coins = [int(x) for x in input('Enter coins: ').split()]
change = int(input('Enter change: '))
print(countChange(coins, len(coins), change))
