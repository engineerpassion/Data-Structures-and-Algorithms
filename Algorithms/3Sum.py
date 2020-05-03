import time
from BinarySearch import binary_search

def three_sum_count(a, sum_val):
    count = 0
    if a is not None and len(a) >= 3:
        n = len(a)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if a[i] + a[j] + a[k] == sum_val:
                        count += 1
    return count

def modified_three_sum_count(a, sum_val):
    count = 0
    if a is not None and len(a) >= 3:
        n = len(a)
        a.sort()
        for i in range(n):
            for j in range(i + 1, n):
                val_to_find = sum_val - a[i] - a[j]
                if a[i] < a[j] and a[j] < val_to_find: # To avoid duplicate counting
                    k = binary_search(a, val_to_find)
                    if k is not None and k != i and k != j:
                        count += 1
    return count

def main():
    a = [30, -40, -20, -10, 40, 0, 10, 5]
    print("My list is {}".format(a))
    print()
    start_time = time.time()
    count = three_sum_count(a, 0)
    end_time = time.time()
    print("The brute-force N^3 solution gives {} counts for 0 sum in {} seconds.".format(count, (end_time - start_time)))
    print()
    start_time = time.time()
    count = modified_three_sum_count(a, 0)
    end_time = time.time()
    print("The sort and binary search solution gives {} counts for 0 sum in {} seconds.".format(count, (end_time - start_time)))
    print()

"""
Uncomment the following line to run the file.
"""
#main()