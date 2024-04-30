"""
Find the first and last index of a target in an array using binary search.
***Need to fix edge cases***
"""


def bin_search_last(left, right, array, target):
    mid = (left + right) // 2
    if left == mid:
        return -1
    if array[mid] == target and array[mid + 1] > target:
        return mid
    elif array[mid] == target or array[mid] < target:
        return bin_search_last(mid, right, array, target)
    elif array[mid] > target:
        return bin_search_last(left, mid, array, target)


def bin_search_first(left, right, array, target):
    mid = (left + right) // 2
    if left == mid:
        return -1
    if array[mid] == target and array[mid - 1] < target:
        return mid
    elif array[mid] == target or array[mid] > target:
        return bin_search_first(left, mid, array, target)
    elif array[mid] < target:
        return bin_search_first(mid, right, array, target)


def find_indices(array, target):
    first = bin_search_first(0, len(array) - 1, array, target)
    last = bin_search_last(0, len(array) - 1, array, target)
    print(first, last)


def main():
    array = [
        1,
        2,
        3,
        5,
        5,
        5,
        5,
        5,
        5,
    ]
    target = 5  # -> 4 , 7
    find_indices(array, target=target)


if __name__ == "__main__":
    main()
