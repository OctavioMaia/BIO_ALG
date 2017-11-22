# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:05:05 2017

@author: Joao
"""

class subsMatrix:
    def __init__(self):
        self.alphabet=""
        self.sm={}
        
    def createFromMatch(self,match,mismatch,alphabet):
        self.alphabet=alphabet
        for c1 in alphabet:
            for c2 in alphabet:
                if (c1==c2):
                    self.sm[c1+c2]=match
                else:
                    self.sm[c1+c2]=mismatch
                
    def scorePair (self,c1,c2):
        if (not c1 in self.alphabet or not c2 in self.alphabet):
            return None    
        else:
            return self.sm[c1+c2]
        
    def getItem (self,ij):
        i,j=ij
        return self.scorePair(i,j)        
    
    def test1():
        sm=subsMatrix()
        sm.loadFromFile("blosum62.mat","\t")
        print(sm.alphabet)
        print(sm.scorePair("G","M"))
        print(sm.scorePair["G","M"])