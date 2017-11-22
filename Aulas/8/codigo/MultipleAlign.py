from MyAlign import MyAlign
from MySeq import MySeq
from AlignSeq import AlignSeq
from SubstMatrix import SubstMatrix

class MultipleAlign(object):
    def __init__(self, seqs, alignseq):
        self.seqs = seqs
        self.alignpars = alignseq
    
    def scoreColumn (self, charsCol):
        sc = 0;
        for i in range(len(charsCol)):
            for j in range(i+1, len(charsCol)):
                if charsCol[i]!='-' or charsCol[j]!='-':
                    sc += self.alignpars.scorePos(charsCol[i], charsCol[j]) 
        #print (sc)
        return sc
     
    def scoreSP (self, alinhamento):
        sp = 0
        ncols = len(alinhamento[0])
        
        for j in range(ncols):
            charsCol = alinhamento.column(j)
            scoreCol = self.scoreColumn(charsCol)
            sp += scoreCol
        return sp
    
    def addSeqAlignment (self, alignment, seq):
        res = []
        for i in range(len(alignment.listseqs)+1):
            res.append("")
        cons = MySeq(alignment.consensus(),alignment.tipo)
        self.alignpars.needlemanWunsch(cons, seq)
        align2 = self.alignpars.recoverAlignment()
        orig = 0
        for i in range(len(align2)):
            if align2[0,i]== '-':
                for k in range(len(alignment.listseqs)):
                    res[k] += "-"
            else:
                for k in range(len(alignment.listseqs)):
                    res[k] += alignment[k,orig]
                orig+=1
        res[len(alignment.listseqs)] = align2.listseqs[1]
        return MyAlign(res, alignment.tipo)
    
    def alignConsensus(self):
        self.alignpars.needlemanWunsch(self.seqs[0], self.seqs[1])
        res = self.alignpars.recoverAlignment()

        for i in range(2, len(self.seqs)):
            res = self.addSeqAlignment(res, self.seqs[i])
        return res

def test():  
    s1 = MySeq("PHWAS","protein")
    s2 = MySeq("HWASW","protein")
    s3 = MySeq("HPHWA","protein")
    sm = SubstMatrix()
    sm.loadFromFile("blosum62.mat", "\t")
    aseq = AlignSeq(sm, -8)
    ma = MultipleAlign([s1,s2,s3], aseq)
    alinm = ma.alignConsensus()
    print(ma.scoreSP(alinm))
    print(alinm)

# -PHWAS-
# --HWASW
# HPHWA--

def test2():  
    s1 = MySeq("SWSSKLMKKIM","protein")
    s2 = MySeq("SYSLMKLKSWK","protein")
    s3 = MySeq("SWSSLMKLILS","protein")
    s4 = MySeq("SWSLMKLISSW","protein")
    sm = SubstMatrix()
    sm.loadFromFile("blosum62.mat", "\t")
    aseq = AlignSeq(sm, -8)
    ma = MultipleAlign([s1,s2,s3, s4], aseq)
    alinm = ma.alignConsensus()
    print(alinm) 
    print(ma.scoreSP(alinm))

#SWSSKLMKKIM--
#SYSLMKLKSWK--
#SWSS-LMKLILS-
#SWS--LMKLISSW
#30

if __name__ == "__main__": 
    test()
    test2()