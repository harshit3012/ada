def kruskals(graph):
    graph.sort(key=lambda e: e[2])
    set_included = set()
    for edge in graph:
        if edge[0] not in set_included or edge[1] not in set_included:
            print(edge[0], '->', edge[1], '=', edge[2])
            set_included.add(edge[0])
            set_included.add(edge[1])


edges = int(input("Enter number of edges: "))
n_vertices = int(input("Enter number of vertices: "))
graph = []
print(f'Enter {edges} edges [start] [end] [weight]: ')
for i in range(edges):
    start, end, weight = [int(x) for x in input().split()]
    graph.append((start, end, weight))

kruskals(graph)
