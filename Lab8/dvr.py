class Network():
    def __init__(self, N):
        self.matrix = []
        self.N = N

    def addlink(self, u, v, w):
        self.matrix.append((u, v, w))

    def table(self, dist, src):
        print(f"Vector Table of {chr(ord('A')+src)}")
        print("Dest\tCost")
        for i in range(self.N):
            print(f"{chr(ord('A')+i)}\t{dist[i]}")

    def algorithm(self, src):
        dist = [99] * self.N
        dist[src] = 0

        for _ in range(self.N - 1):
            for u, v, w in self.matrix:
                if dist[u] != 99 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        self.table(dist, src)


if __name__ == "__main__":

    matrix = []
    n = int(input("Enter Number of Nodes : "))
    print("Enter the Adjacency Matrix : ")

    for _ in range(n):
        m = list(map(int, input().split(" ")))
        matrix.append(m)

    g = Network(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                g.addlink(i, j, 1)

    for _ in range(n):
        g.algorithm(_)
