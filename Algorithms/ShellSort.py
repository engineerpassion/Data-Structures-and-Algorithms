def swap(a, i, j):
    c = a[i]
    a[i] = a[j]
    a[j] = c
    return a

def h_sort(a, h):
    if a is not None and len(a) > 1:
        n = len(a)
        for i in range(0, n):
            for j in range(i, 0, -h):
                if a[j] < a[j - 1]:
                    a = swap(a, j, j - 1)
                elif a[j] > a[j - 1]:
                    break
    return a

def shell_sort(a):
    if a is not None and len(a) > 1:
        n = len(a)
        h = 1
        while h < n/3:
            h = int(3 * h + 1)
        while h >= 1:
            a = h_sort(a, h)
            h = int(h/3)
    return a

def main():
    a = [5, 4, 3, 3, 2, 1]
    print("My list looks as follows:")
    print(a)
    a = shell_sort(a)
    print("My sorted list using shell sort looks as follows:")
    print(a)

"""
Uncomment the following line to run the file.
"""
#main()