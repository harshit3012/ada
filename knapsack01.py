val = list(map(int, input('Enter values: ').split()))
weights = list(map(int, input('Enter weights: ').split()))
bweight = int(input('Enter bag weight: '))


def knapSack(val, weights, bweight):
    dynamic_pro_array = [[0] * (bweight + 1)] * (len(val) + 1)
    for i in range(len(weights) + 1):
        for j in range(bweight + 1):
            if i == 0 or j == 0:
                dynamic_pro_array[i][j] == 0
            elif weights[i - 1] <= j:
                dynamic_pro_array[i][j] = max(
                    val[i - 1] + dynamic_pro_array[i - 1][j - weights[i - 1]], dynamic_pro_array[i - 1][j])
            else:
                dynamic_pro_array[i][j] = dynamic_pro_array[i - 1][j]
    return dynamic_pro_array[len(val)][bweight]


print(knapSack(val, weights, bweight))
