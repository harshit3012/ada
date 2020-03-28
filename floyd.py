n = int(input('Enter number of vertices: '))
adj_mat = [[0] * n] * n
for i in range(n):
    adj_mat[i] = list(map(int, input().split()))

result = adj_mat.copy()
for k in range(n):
    for i in range(n):
        for j in range(n):
            result[i][j] = min(result[i][j], result[i][k] + result[k][j])

print(result)
