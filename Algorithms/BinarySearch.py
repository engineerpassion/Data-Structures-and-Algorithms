def binary_search(a, key):
    idx = None
    low = 0
    high = len(a) - 1
    while low <= high:
        middle = int((low + high) / 2)
        if key > a[middle]:
            low = middle + 1
        elif key < a[middle]:
            high = middle - 1
        else:
            idx = middle
            break
    return idx

def recursive_binary_search(a, key, low=None, high=None):
    if low is None or high is None:
        low = 0
        high = len(a)
    if low > high:
        return None
    middle = int((low + high) / 2)
    if a[middle] > key:
        return recursive_binary_search(a, key, low, middle - 1)
    elif a[middle] < key:
        return recursive_binary_search(a, key, middle + 1, high)
    else:
        return middle

def main():
    a = [10, 25, 30, 45, 60, 70, 85, 100]
    print("My list is {}".format(a))
    print()
    print("Regular Binary Search:")
    print()
    print("Element 25 is at index {}.".format(binary_search(a, 25)))
    print("Element 85 is at index {}.".format(binary_search(a, 85)))
    print("Element 55 is at index {}.".format(binary_search(a, 55)))
    print()
    print("Recursive Binary Search:")
    print()
    print("Element 25 is at index {}.".format(recursive_binary_search(a, 25)))
    print("Element 85 is at index {}.".format(recursive_binary_search(a, 85)))
    print("Element 55 is at index {}.".format(recursive_binary_search(a, 55)))

"""
Uncomment the following line to run the file.
"""
#main()