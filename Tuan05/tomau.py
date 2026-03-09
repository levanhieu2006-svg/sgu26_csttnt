def docFile(fpath="TOMAU.INP"):
    with open(fpath,"rt") as f:
        n = int(f.readline().strip())
        adj = {i: [] for i in range(1,n+1)}
        for line in f:
            u,v = map(int,line.split())
            adj[u].append(v)
            adj[v].append(u)
    return n, adj

def toMauDoThi(n, adj):
    degree = [(i,len(adj[i])) for i in range(1,n+1)]
    degree.sort(key=lambda x: x[1], reverse=True)

    color = [0]*(n+1)
    for node,_ in degree:
        used = set()
        for nb in adj[node]:
            if color[nb] != 0:
                used.add(color[nb])
        c = 1
        while c in used:
            c += 1
        color[node] = c
    k = max(color)
    print(k)
    for i in range(1,k+1):
        group = []
        for v in range(1,n+1):
            if color[v] == i:
                group.append(v)
        print(*group)
def main():
    n, adj = docFile()
    toMauDoThi(n, adj)
if __name__ == "__main__":
    main()