def insertion_sort(items):
    items_size = len(items)
    for j in range(1, items_size):
        key = items[j]
        i = j - 1
        while i >= 0 and items[i] > key:
            items[i + 1] = items[i]
            i -= 1
        items[i + 1] = key

    return items


if __name__ == '__main__':
    arr = [6, 3, 2, 9, 5]
    sorted_list = insertion_sort(arr)
    print(sorted_list)
# [6,3,2,9,5]
# j=2
# key=2
# i=1
# A[i]=6
# i>=0 and A[i] > key : True
# A[1]=3
# A[0]=2
# [2,3,6,9,5]
