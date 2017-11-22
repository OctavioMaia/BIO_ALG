# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:21:49 2017

@author: Joao
"""

n=10
mat1=[[0,1,2,3],[4,5,6,7],[8,9,10,11]]
mat2=[[5,4,2],[6,3,7],[10,29,34],[40,52,51]]

def createIdent(n):
    new=[]
    for r in range(n):
        new.append([0]*n)
        new[r][r]=1
    return new

def printMatrix(mat):
    for lin in range(0,len(mat)):
        print (mat[lin])
        
def createMat(l,c):
    new=[]
    for r in range(l):
        new.append([0]*c)
    return new    
    
def getLine(l,mat):
    return mat[l]

def getColumn(c,mat):
    new=[]
    for r in range(0,len(mat)):
        new.append(mat[r][c])
    return new

def setLine(n,l,mat):
    mat[l]=n
    return mat

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

def sumLine(mat):
    s=[]
    for r in range(0,len(mat)):
        add=0.0
        for c in range(0,len(mat[r])):
            add+=mat[r][c]
        s.append(add)
    return s

def sumColumn(mat):
    s=[0]*len(mat[0])
    for r in range(0,len(mat)):
        for c in range(0,len(mat[r])):
            s[c]+=mat[r][c]
    return s

def addLine(mat,new):
    mat.append(new)
    return mat

def delLine(mat,line):
    del(mat[line])
    return mat

def addColumn(mat,new):
    for r in range(0,len(mat)):
        mat[r].append(new[r])
    return mat

def delColumn(mat,col):
    for r in range(0,len(mat)):
        del(mat[r][col])
    return mat
"""
def normalizeZScore(mat):
    mean=meanMat(mat)
    sd=np.std(mat)
    newmat=copiaMat(mat)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            newmat[i][j]=(newmat[i][j]*mean)/sd
    return newmat
"""
def freqMatrixDNA(lst_seq):
    nc=len(lst_seq)
    fm=createMat(4,nc)
    for seq in lst_seq:
        for bp,index in enumerate(seq):
            if bp == "A":
                fm[0][index]+=1
            if bp == "C":
                fm[1][index]+=1
            if bp == "G":
                fm[2][index]+=1
            if bp == "T":
                fm[3][index]+=1
    return fm
