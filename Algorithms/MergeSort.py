def merge(a, low, middle, high, aux):
    i = k = low
    j = middle + 1
    for idx in range(low, high + 1):
        aux[idx] = a[idx]
    while k <= high:
        if i > middle:
            a[k] = aux[j]
            j += 1
        elif j > high:
            a[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            a[k] = aux[i]
            i += 1
        else:
            a[k] = aux[j]
            j += 1
        k += 1
    return a

def merge_sort(a, low=None, high=None, aux=None):
    if a is not None and len(a) > 1:
        n = len(a)
        low = 0 if low is None else low
        high = n - 1 if high is None else high
        aux = [0] * n if aux is None else aux
        if low < high:
            middle = (low + high) // 2
            a = merge_sort(a, low=low, high=middle, aux=aux)
            a = merge_sort(a, low=middle + 1, high=high, aux=aux)
            if a[middle] > a[middle + 1]:
                # Merging only when the two sorted sub-arrays needs to be merged
                a = merge(a, low, middle, high, aux)
    return a

def main():
    a = [5, 4, 3, 3, 2, 1]
    print("My list looks as follows:")
    print(a)
    a = merge_sort(a)
    print("My sorted list using insertion sort looks as follows:")
    print(a)

"""
Uncomment the following line to run the file.
"""
#main()