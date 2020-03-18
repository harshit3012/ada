#This program does topological sorting
edges = int(input("enter number of edges: "))
n_vertices = int(input("enter number of vertices: "))
neighbours_dict = {}
print("enter edges [start] [end]: ")
for i in range(edges):
    start, end = [int(x) for x in input().split()]
    if not neighbours_dict.get(start):
        neighbours_dict[start] = [end]
    else:
        neighbours_dict[start].append(end)
    
def topOrder(node, visited, stack):
    visited[node] = True

    if neighbours_dict.get(node):
        for n in neighbours_dict[node]:
            if not visited[n]:
                topOrder(n, visited, stack)
    
    stack.append(node)

visited = [False] * n_vertices
main_stack = []
for vertex in neighbours_dict.keys():
    if not visited[vertex]:
        topOrder(vertex, visited, main_stack)
print(main_stack[::-1])
