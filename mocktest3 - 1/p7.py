def f(arr2D):
    num_col = len(arr2D[0])

    col_sums = []

    for col in range(num_col):
        col_sum = sum(row[col] for row in arr2D)
        if col_sum in col_sums:
            return True
        col_sums.append(col_sum)
    
    return False

print(f([[3,4,2],[5,1,6]]))
print(f([[3,4,2],[5,1,7]]))
print(f([[3,4],[5,1],[4,7]]))  # True
print(f([[3,4],[5,9],[4,7]]))  # False