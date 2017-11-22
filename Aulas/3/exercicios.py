def createZeroMatrix(linhas,colunas):
    new = []
    for l in range(linhas):
        new.append([0]*colunas)

    return new

def getRow(mat,nr):
    return mat[nr]

def setRow(mat,nr,row):
    mat[nr]=row
    return mat

def getColumn(mat,nc):
    col = []
    for r in range(len(mat)):
        col.append(r[nc])
    return col

def setColumn(n,c,mat):
    for r in range(0,len(mat)):
        mat[r][c]=n
    return mat

def sumMat(mat):
    s=0.0
    for r in range(0,len(mat)):
        for c in range(0,len(mat[r])):
            s+=mat[r][c]
    return s

def meanMat(mat):
    s=0.0
    n=0
    for r in range(0,len(mat)):
        for c in range(0,len(mat[r])):
            s+=mat[r][c]
            n+=1
    return s/n