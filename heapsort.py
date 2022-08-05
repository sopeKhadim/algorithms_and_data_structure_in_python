def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i

    if left(i) < n and arr[i] < arr[left(i)]:
        largest = left(i)
        print("First condition")
        print(arr[i], " < ", arr[left(i)])

    if right(i) < n and arr[largest] < arr[right(i)]:
        largest = right(i)
        print("Second condition")
        print(arr[largest], " < ", arr[right(i)])

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        print("Third condition")
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2, -1, -1):
        print("i =", i)
        heapify(arr, n, i)

    print("Finished First steps")
    print(arr)

    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)


if __name__ == '__main__':

    arr = [1, 12, 9, 5, 6, 10]
    heapsort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d " % arr[i], end='')

# i=3
# 2
#
#
