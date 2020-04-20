class WeightedPathCompressionQuickUnionUF():
    def __init__(self, n):
        self.n = n
        self.ar = [i for i in range(self.n)]
        self.weights = [1 for i in range(self.n)]
    
    def union(self, p, q):
        root_p = self._find_root(p)
        root_q = self._find_root(q)
        if root_p != root_q:
            if self.weights[p] <= self.weights[q]:
                # p is in smaller or equal tree
                self.ar[root_p] = root_q
                self.weights[root_q] += self.weights[root_p]
            else:
                # q is in smaller tree
                self.ar[root_q] = root_p
                self.weights[root_p] += self.weights[root_q]
        return
    
    def connected(self, p, q):
        con = False
        if self._find_root(p) == self._find_root(q):
            con = True
        return con
    
    def _find_root(self, a):
        root = None
        parent = self.ar[a]
        while parent != self.ar[a]:
            self.ar[a] = self.ar[self.ar[a]] # The PATH COMPRESSION LINE
            parent = self.ar[parent]
        root = parent
        return root

def main():
    uf = WeightedPathCompressionQuickUnionUF(10)
    print("Initial Quick Find UF:")
    print(uf.ar)
    uf.union(4, 3)
    print("Union (4, 3).")
    uf.union(3, 8)
    print("Union (3, 8).")
    uf.union(6, 5)
    print("Union (6, 5).")
    uf.union(9, 4)
    print("Union (9, 4).")
    uf.union(2, 1)
    print("Union (2, 1).")
    print("Quick Find UF:")
    print(uf.ar)
    print("connected(0, 7): {}".format(uf.connected(0, 7)))
    print("connected(8, 9): {}".format(uf.connected(8, 9)))
    uf.union(5, 0)
    print("Union (5, 0).")
    uf.union(7, 2)
    print("Union (7, 2).")
    uf.union(6, 1)
    print("Union (6, 1).")
    uf.union(1, 0)
    print("Union (1, 0).")
    print("connected(0, 7): {}".format(uf.connected(8, 9)))
    print("Final Quick Find UF:")
    print(uf.ar)

"""
Uncomment the following line to run the file.
"""
#main()