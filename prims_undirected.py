n_vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))
dict_graph = {} 
print("Enter edges in the form [vertice_start] [end] [weight]: ")
for i in range(edges):
    start, end, weight = [int(x) for x in input().split()]
    if not dict_graph.get(start):
        dict_graph[start] = [(end, weight)]
    else:
        dict_graph[start].append((end, weight))
    if not dict_graph.get(end):
        dict_graph[end] = [(start, weight)]
    else:
        dict_graph[end].append((start, weight))


def prims(dict_graph, startVertex):
    selected = set([startVertex])
    for no_edges in range(len(dict_graph.keys()) - 1):
        end = None
        start = None
        weight = int(100000000000)
        for startV in selected:
            for endV in dict_graph[startV]:
                if endV[1] < weight and endV[0] not in selected:
                    start, end, weight = startV, endV[0], endV[1]
        print(f"{start} -> {end} = {weight}")
        selected.add(end)


prims(dict_graph, 1)
