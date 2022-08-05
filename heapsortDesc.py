def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def heapify(arr, n, i):
    shortest = i

    if left(i) < n and arr[i] > arr[left(i)]:
        shortest = left(i)

    if right(i) < n and arr[shortest] > arr[right(i)]:
        shortest = right(i)

    if shortest != i:
        arr[i], arr[shortest] = arr[shortest], arr[i]
        heapify(arr, n, shortest)


def heapsort_desc(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':

    arr = [1, 12, 9, 5, 6, 10]
    heapsort_desc(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d " % arr[i], end='')
