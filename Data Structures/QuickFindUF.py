class QuickFindUF():
    def __init__(self, n):
        self.n = n
        self.ar = [i for i in range(self.n)]
    
    def union(self, a, b):
        val_a = self.ar[a]
        val_b = self.ar[b]
        for i in range(self.n):
            if self.ar[i] == val_b:
                self.ar[i] = val_a
        return
    
    def connected(self, a, b):
        connected = False
        if self.ar[a] == self.ar[b]:
            connected = True
        return connected

def main():
    uf = QuickFindUF(10)
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