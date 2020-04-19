def bfs(graph, visited, queue):
    while len(queue) > 0:
        curr_node = queue.pop(0)
        visited[curr_node] = True
        if not graph.get(curr_node):
            continue
        for i in graph[curr_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return visited

n = int(input("Enter no of vertices: "))
e = int(input("Enter no of edges: "))
print("Enter the edges : ")
graph = {}
for i in range(e):
    start, end = [int(j) for j in input("").split()]
    if not graph.get(start):
        graph[start] = set([end])
    else:
        graph[start].add(end)
    if not graph.get(end):
        graph[end] = set([start])
    else:
        graph[end].add(start)

visited = [False]*n
queue = [0]
visited[0] = True
visited_nodes = bfs(graph, visited, queue)
count = 0
for i in visited_nodes:
    if i:
        count += 1
if count == n: print("Connected")
else: print("Not Connected")