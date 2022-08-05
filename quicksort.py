

def partition(arr, p, r):
    x = arr[r]  # pivot
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i + 1


def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


if __name__ == '__main__':

    arr = [1, 12, 9, 5, 6, 10]
    quicksort(arr, 0, len(arr) - 1)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d " % arr[i], end='')
