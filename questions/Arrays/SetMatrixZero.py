matrix = [[1, 2, 3,0],
          [4, 0, 6,1],
          [7, 8, 9,5]]

def brute():
    def setRow(rows, i):
        for j in range(rows):
            if matrix[j][i] != 0:
                matrix[j][i] = -1

    def setColumn(columns, j):
        for i in range(columns):
            if matrix[j][i] != 0:
                matrix[j][i] = -1

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                setRow(rows, i)
                setColumn(columns, j)

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

# brute()

def better():
    rows = [0]*len(matrix)
    cols = [0]*len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows[i] = 1
                cols[j] = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rows[i] or cols[j]:
                matrix[i][j] = 0

# better()

def optimal():
    col0 = 1
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    for i in range(1,row):
        for j in range(1,col):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(col):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(row):
            matrix[i][0] = 0

optimal()
for i in matrix:
    print(i, end='\n')
