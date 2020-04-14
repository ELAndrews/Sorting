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


a = [1, 2, 4, 5, 9]
b = [3, 6, 7, 8]

print(merge(a, b))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


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
