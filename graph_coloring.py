class GraphColor:
    def __init__(self, v, edges, k):
        self.v = v
        self.k = k
        self.col = [0] * self.v
        self.g = [[0] * v for _ in range(v)]
        for u, v in edges:
            self.g[u][v] = 1
            self.g[v][u] = 1
    
    def color(self, node=0):
        if node == self.v:
            return True
        
        for c in range(1, self.k + 1):
            if self.valid(node, c):
                self.col[node] = c
                if self.color(node + 1):
                    return True
                self.col[node] = 0
        
        return False
    
    def valid(self, node, c):
        for i in range(self.v):
            if self.g[node][i] == 1 and self.col[i] == c:
                return False
        return True
    
    def show(self):
        print(f"Possible with {self.k} colors")
        print("Assignment:", self.col)


def main():
    n, m, k = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    
    graph = GraphColor(n, edges, k)
    if graph.color():
        graph.show()
    else:
        print(f"Not possible with {k} colors")


main()
