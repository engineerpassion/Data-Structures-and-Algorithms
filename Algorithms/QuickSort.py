def swap(a, i, j):
    c = a[i]
    a[i] = a[j]
    a[j] = c
    return a

def partition(a, low, high):
    i = low + 1
    j = high
    while True:
        while a[i] < a[low]:
            i += 1
            if i == high:
                break
        while a[low] < a[j]:
            j -= 1
            if j == low:
                break
        if i >= j:
            break
        swap(a, i, j)
    swap(a, low, j)
    return j

def quick_sort(a, low=None, high=None):
    if a is not None and len(a) > 1:
        n = len(a)
        low = 0 if low is None else low
        high = n - 1 if high is None else high
        if high > low:
            partitioned_idx = partition(a, low, high)
            a = quick_sort(a, low, partitioned_idx - 1)
            a = quick_sort(a, partitioned_idx + 1, high)
    return a

def main():
    a = [5, 4, 3, 3, 2, 1]
    print("My list looks as follows:")
    print(a)
    a = quick_sort(a)
    print("My sorted list using quick sort looks as follows:")
    print(a)

"""
Uncomment the following line to run the file.
"""
#main()