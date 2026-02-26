print("Hello, World!")

def coo(densemat, rows, cols):
    val = []
    row = []
    col = []

    for r in range(rows):
        for c in range(cols):
            if densemat[r][c] != 0:
                val.append(densemat[r][c])
                row.append(r)
                col.append(c)
    return val, row, col

def makecsr(densemat, rows, cols):
    # val, colindex, rowptr
    val = []
    colindex = []
    rowptr = [0]
    nnzcount = 0
    for r in range(rows):
        for c in range(cols):
            if densemat[r][c] != 0:
                val.append(densemat[r][c])
                colindex.append(c)
                nnzcount += 1
        rowptr.append(nnzcount)

    return val, colindex, rowptr

def csc(densemat, rows, cols):

    val = []
    row = []
    colptr = [0]
    nnzcol = 0

    for c in range(cols):
        for r in range(rows):
            if densemat[r][c] != 0 :
                val.append(densemat[r][c])
                row.append(r)
                nnzcol += 1
        colptr.append(nnzcol)

    return val, row, colptr

def spmv(val:list, colindex:list, rowptr:list, vector:list):

    result = [0] * (len(rowptr)-1)

    for  r  in  range(len(rowptr) - 1):
        startofrow = rowptr[r]
        endofrow = rowptr[r + 1]

        accum = 0
        for index in range(startofrow, endofrow):
            A = val[index]
            vectorelem = vector[colindex[index]]
            accum += A * vectorelem

        result[r] += accum
    
    return result


if __name__ == "__main__":
    dense_mat = [
        [0, 0, 1, 0, 2],
        # [0, 0, 0, 0, 0],
        [4, 0, 0, -2, 0],
        [0, 0, 3, 0, 0]
    ]
    vector = [1, 2, 3, 4, 5]

    rows = len(dense_mat)
    cols = len(dense_mat[0])
    val, colindex, rowptr = makecsr(dense_mat, rows, cols)
    print(f"val: {val}, \ncolindex: {colindex}, \nrowptr: {rowptr}")


    y = spmv(val, colindex, rowptr, vector)
    print(f"y: {y}")
     
    # print("CSC:")
    # val, row, colptr = csc(dense_mat, rows, cols)
    # print(f"val: {val}, \nrow: {row}, \ncolptr: {colptr}")

    # print("COO:")
    # val, row, col = coo(dense_mat, rows, cols)
    # print(f"val: {val}, \nrow: {row}, \ncol: {col}")
