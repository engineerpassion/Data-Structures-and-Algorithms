import random

def swap(a, i, j):
    c = a[i]
    a[i] = a[j]
    a[j] = c
    return a

def knuth_shuffle(a):
    if a is not None and len(a) > 1:
        n = len(a)
        for i in range(1, n):
            index_to_swap = random.randint(0, i)
            a = swap(a, i, index_to_swap)
    return a

def main():
    a = [5, 4, 3, 3, 2, 1]
    print("My list looks as follows:")
    print(a)
    a = knuth_shuffle(a)
    print("My shuffled list using Knuth Shuffle algorithm looks as follows:")
    print(a)

"""
Uncomment the following line to run the file.
"""
#main()
