def swap(a, i, j):
    c = a[i]
    a[i] = a[j]
    a[j] = c
    return a

def insertion_sort(a):
    if a is not None and len(a) > 1:
        n = len(a)
        for i in range(0, n):
            for j in range(i, 0, -1):
                if a[j] < a[j - 1]:
                    a = swap(a, j, j - 1)
                elif a[j] > a[j - 1]:
                    break
    return a

def main():
    a = [5, 4, 3, 3, 2, 1]
    print("My list looks as follows:")
    print(a)
    a = insertion_sort(a)
    print("My sorted list using insertion sort looks as follows:")
    print(a)

"""
Uncomment the following line to run the file.
"""
#main()