def merge(items, p, q, r):
    left = items[p:q+1]
    right = items[q+1:r+1]
    i = j = 0
    k = p

    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1
        k += 1
    if j == len(right):
        items[k:r+1] = left[i:]


def mergesort(items, p, r):
    if p < r:
        q = (p+r)//2
        mergesort(items, p, q)
        mergesort(items, q+1, r)
        merge(items, p, q, r)


if __name__ == '__main__':
    items = [6, 8, 3, 7, 2, 9, 5]
    mergesort(items, 0, len(items)-1)
    print(items)
