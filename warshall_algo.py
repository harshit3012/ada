n = int(input('Enter number of vertices: '))
adj_mat = [[0] * n] * n
print("Enter the adjacency matrix :")
for i in range(n):
    adj_mat[i] = list(map(int, input().split()))

adj_mat_t_c = adj_mat
for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj_mat_t_c[i][j] == 1:
                continue
            elif adj_mat_t_c[i][k] == 1 and adj_mat_t_c[k][j] == 1:
                adj_mat_t_c[i][j] = 1

print(adj_mat_t_c)
