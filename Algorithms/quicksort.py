"""
Implementation of quicksort
"""


def choosePivot(array, left, right):
    mid = (left + right) // 2
    a = array[left]
    b = array[mid]
    c = array[right]
    if a >= b and a <= c or a <= b and a >= c:
        return left
    elif b >= a and b <= c or b <= a and b >= c:
        return mid
    else:
        return right


def partition(array, left, right):
    i = left - 1
    pivot_index = choosePivot(array, left, right)
    array[pivot_index], array[right] = array[right], array[pivot_index]
    pivot = array[right]

    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quicksort(array, left, right):
    if left < right:
        pivot_index = choosePivot(array, left, right)
        new_pivot_index = partition(array, left, right)
        quicksort(array, left, new_pivot_index - 1)
        quicksort(array, new_pivot_index + 1, right)


def main():
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] * 100
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)


if __name__ == "__main__":
    main()
