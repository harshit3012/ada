"""
import string
n = int(input("Enter the number of nodes : "))
out_graphs1 = {}
for i in list(string.ascii_lowercase)[0:n]:
    print("Enter the nodes directed by node "+i, end=": ")
    out_graphs1[i] = [j for j in input().split()]
print(out_graphs1.keys())
visited = {}
for i in list(out_graphs1.keys()):
"""
from collections import defaultdict 
  
class fin_graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]: 
            if !visited[neighbour]: 
                if self.isCyclicUtil(neighbour, visited, recStack): 
                    return True
            elif recStack[neighbour]: 
                return True
        recStack[v] = False
        return False

    def isCyclic(self): 
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if ivisited[node]: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False 
g = fin_graph(6) 
g.addEdge(0, 4) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 5) 
g.addEdge(2, 3) 
g.addEdge(3, 6)
g.addEdge(4, 3)
g.addEdge(4, 6)
g.addEdge(5, 4)
g.addEdge(6, 0)

if g.isCyclic(): 
    print("Graph has a cycle")
else: 
    print("Graph has no cycle")
  
