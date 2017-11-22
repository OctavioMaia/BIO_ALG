# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:11:19 2017

@author: Joao
"""

seq1=["A","T","C","T","G","A","T"]
seq2=["A","C","C","T","G","C","C"]

def createMat (s1,s2):
    mat=[]
    for r in range(0,len(s1)):
        mat.append([0]*len(s2))
    return mat    

def dotPlot (s1,s2):
    mat=createMat(s1,s2)
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if(s1[i]==s2[j]): 
                mat[i][j]=1
    return mat

def printMatrix(mat):
    for lin in range(0,len(mat)):
        print (mat[lin])
        
def windowPlot(s1,s2,stValue,wSize):
    mat=createMat(s1,s2)
    start=int(wSize/2)
    for i in range(start,len(s1)-start):
        for j in range(start,len(s2)-start):
            matches=0
            l==i-start
            for k in range(i-start,i+start+1):
                if(s1[k]==s2[k]): matches+=1
                l+=1
            if matches >= stValue: mat[i][j]=1
    return mat
            