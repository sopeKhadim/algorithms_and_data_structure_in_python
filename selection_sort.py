def selection_sort(items):
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[min_index] > items[j]:
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]

    return items


if __name__ == '__main__':
    arr = [6, 8, 3, 7, 2, 9, 5]
    sorted_list = selection_sort(arr)
    print(sorted_list)
