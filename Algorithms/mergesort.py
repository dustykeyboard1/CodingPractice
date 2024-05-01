"""
Find the kth largest element using merge sort. 
"""

INF = float("inf")


def merge(left, right):
    sorted = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    while i < len(left):
        sorted.append(left[i])
        i += 1

    while j < len(left):
        sorted.append(left[j])
        j += 1

    return sorted


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort

    return merge(left, right)


def main():
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f" The sorted array is: {merge_sort(array)}")


if __name__ == "__main__":
    main()
