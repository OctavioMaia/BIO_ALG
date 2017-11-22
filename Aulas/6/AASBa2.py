# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#1
def patternSearch (seq, pat):
    for i in range(0,len(seq)-len(pat)+1):
        if seq[i:i+len(pat)]==pat:
            return i
    return -1
        
def allPattern (seq, pat):
    index=[]
    for i in range(0,len(seq)-len(pat)+1):
        if seq[i:i+len(pat)]==pat:
            index.append(i)        
    return index

#2
def enumWords (seq,k):
    words={}
    for i in range(0,len(seq)-k+1):
        w=seq[i:i+k]
        if w in words:
            words[w]+=1
        else:
            words[w]=1
    for k in words.keys():
        print( k+" -> "+str(words[k]))
    
#3
