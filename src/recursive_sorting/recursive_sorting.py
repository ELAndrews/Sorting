import math

# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    countA = 0
    countB = 0

    for i in range(0, elements):
        if countA == len(arrA):
            merged_arr[i] = arrB[countB]
            countB += 1
        elif countB == len(arrB):
            merged_arr[i] = arrA[countA]
            countA += 1
        elif arrA[countA] < arrB[countB]:
            merged_arr[i] = arrA[countA]
            countA += 1
        elif arrA[countA] > arrB[countB]:
            merged_arr[i] = arrB[countB]
            countB += 1

    return merged_arr


# a = [1, 2, 4, 5, 9]
# b = [3, 6, 7, 8]

# print(merge(a, b))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    arr.sort()

    if len(arr) < 1:
        return arr
    else:
        mid = math.floor(len(arr)/2)
        a = arr[0:mid]
        b = arr[mid:]
        arr = merge(a, b)

    return arr


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# print(merge_sort(arr1))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
