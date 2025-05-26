class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find_parent(x)
        parentY = self.find_parent(y)

        if parentX != parentY:
            # Union by size
            if self.size[parentX] < self.size[parentY]:
                parentX, parentY = parentY, parentX
            self.parent[parentY] = parentX
            self.size[parentX] += self.size[parentY]

    def get_size(self, x):
        return self.size[self.find_parent(x)]


def get_connections(u, v, nodes, queries):
    uf = UnionFind(nodes)

    for a, b in zip(u, v):
        uf.union(a, b)

    return [uf.get_size(user) for user in queries]
    pass
