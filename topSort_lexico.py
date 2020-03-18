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
    
indegrees = [0] * n_vertices 
for vertices in neighbours_dict.values():
    for vertex in vertices:
        indegrees[vertex] += 1
    
noIndegreeVertices = set([n for n in range(6) if not indegrees[n]])
topOrder = []
while len(noIndegreeVertices) > 0:
    min_noIndegreeVertex = min(noIndegreeVertices)
    topOrder.append(min_noIndegreeVertex)
    noIndegreeVertices.discard(min_noIndegreeVertex)
    
    if neighbours_dict.get(min_noIndegreeVertex):
        for neighbour in neighbours_dict[min_noIndegreeVertex]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                noIndegreeVertices.add(neighbour) 

print(topOrder)
