def createIdent(n):
    new = []
    for r in range(n):
        new.append([0]*n)
        new[r][r]=1

    return new

def printMatrix(mat):
    for linha in range(0,len(mat)):
        print(mat[linha])

printMatrix(createIdent(5))