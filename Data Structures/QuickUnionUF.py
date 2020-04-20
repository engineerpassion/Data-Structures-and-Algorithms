class QuickUnionUF():
    def __init__(self, n):
        self.n = n
        self.ar = [i for i in range(self.n)]
    
    def union(self, p, q):
        root_p = self._find_root(p)
        self.ar[root_p] = self._find_root(q)
        return
    
    def connected(self, p, q):
        in_same_com = False
        if self._find_root(p) == self._find_root(q):
            in_same_com = True
        return in_same_com
    
    def _find_root(self, a):
        root = a
        while a != self.ar[a]:
            a = self.ar[a]
        root = a
        return root

def main():
    uf = QuickUnionUF(10)
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

main()