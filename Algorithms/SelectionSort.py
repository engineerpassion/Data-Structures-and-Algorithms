def swap(a, i, j):
    c = a[i]
    a[i] = a[j]
    a[j] = c
    return a

def selection_sort(a):
    if a is not None and len(a) > 1:
        n = len(a)
        for i in range(n):
            sorted_ith_value_index = i
            for j in range(i + 1, n):
                if a[sorted_ith_value_index] > a[j]:
                    sorted_ith_value_index = j
            if sorted_ith_value_index != i:
                a = swap(a, sorted_ith_value_index, i)
    return a

def main():
    a = [5, 4, 3, 3, 2, 1]
    print("My list looks as follows:")
    print(a)
    a = selection_sort(a)
    print("My sorted list using selection sort looks as follows:")
    print(a)

"""
Uncomment the following line to run the file.
"""
#main()