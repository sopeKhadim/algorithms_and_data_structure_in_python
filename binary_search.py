## Recursrive Binary search
def binary_search_rec(tab, left, right, elem):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if tab[mid] == elem:
            return mid
        elif tab[mid] > elem:
            return binary_search_rec(tab, left, mid - 1, elem)
        else:
            return binary_search_rec(tab, mid + 1, right, elem)


# Iterative binary search

def binary_search_iter(tab, elem):
    left = 0
    right = len(tab) - 1

    while left <= right:
        mid = (left + right) // 2
        if tab[mid] == elem:
            return mid
        elif tab[mid] > elem:
            right = mid - 1
        else:
            left = mid + 1

    return None


if __name__ == '__main__':

    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    # result = binary_search_rec(arr, 0, len(arr)-1, x)l
    result = binary_search_iter(arr, x)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
