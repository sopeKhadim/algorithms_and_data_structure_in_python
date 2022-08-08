def rotate_matrix(mat, n):
    mid = n // 2
    for layer in range(mid):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = mat[first][i] # save top
            # left -> top
            mat[first][i] = mat[last - offset][first]
            # bottom -> left
            mat[last - offset][first] = mat[last][last - offset]
            #  right -> bottom
            mat[last][last - offset] = mat[i][last]
            #  top -> right
            mat[i][last] = top  # right <- saved top

    return mat


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    rotate_mat = rotate_matrix(matrix, 4)

    print(rotate_mat)

# rotate_mat = [
# [13, 9, 5, 1],
# [14, 10, 6, 2],
# [15, 11, 7, 3],
# [16, 12, 8, 4]
# ]
