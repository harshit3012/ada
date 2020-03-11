import string
n = int(input("Enter the number of nodes : "))
out_graphs1 = {}
for i in list(string.ascii_lowercase)[0:n]:
    print("Enter the nodes directed by node "+i, end=": ")
    out_graphs1[i] = [j for j in input().split()]
print(out_graphs1.keys())
visited = {}
for i in list(out_graphs1.keys()):
