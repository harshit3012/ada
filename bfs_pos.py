out_graphs = {"a":["b", "f"], "b":["f", "e", "c"], "c":["d"], "d":[], "e":["c", "d", "f"], "f":[]}
def enqueue(list1, rear, ele):
    
    list1[rear]=ele
    rear = rear+1
    return
def dequeue(list1, front, rear):
    if front<rear:
        return list1[front]
        front = front+1
    return -9999
def check1(out_graph_dict, source, dest):
    queue1 = []
    visited = []
    front, rear = 0, 0
    enqueue(queue1, rear, source)
    visited.append(source)
    
    while (dest not in visited) and (front<rear):
        curr = dequeue(queue1, front, rear)
        if curr == -9999:
            print("Not possible to reach destination")
            return False
        visited.extend(out_graph_dict[curr])
        for i in out_graph_dict[curr]:
            enqueue(queue1, rear, i)
    
    return True
source = "a"
dest = "d"
if(check1(out_graphs, source, dest)):
    print("Possible!")
else:
    print("Not Possible!")