for _ in range(int(input())):  # Number of test cases
    n, k = map(int, input().split())  # Read n (grid size) and k (block size)
    mat = [list(map(int, list(input().strip()))) for _ in range(n)]  # Read the n x n grid as characters
    
    res = []
    for i in range(0, n, k):
        curRow = []
        for j in range(0, n, k):
            # Extract the value from the top-left cell of the current block
            curRow.append(mat[i][j])
        res.append(curRow)
    
    # Print the reduced grid
    for row in res:
        print("".join(map(str, row)))
