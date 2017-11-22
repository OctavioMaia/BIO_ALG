class AlignSeq:
    def __init__(self, sm, g):
        self.sm=sm
        self.g=g        #gap
        self.S=None     #score
        self.T=None     #traversal
        self.seq1=None
        self.seq2=None
        
    def scorePos(self,c1,c2):
        if c1 =="-" or c2 =="-":
            return self.g
        else:
            self.sm[c1,c2]
            
    
    def scoreAlign(self, align):
        score=0
        for r in range(align[0]):
            score+=scorePos(align[0][i],align[1][i])
            
    def needlemanWunsch(self, seq1, seq2):
        if seq1.tipo!=seq2.tipo:
            return None
        self.seq1 = seq1
        self.seq2 = seq2
        self.S = [[0]]
        self.T = [[0]]
        for i in range(1,len(seq2)+1):
            self.S[0].append(selg.g*i)
            self.T[0].append(3)
        for j in range(1,len(seq1)+1):
            self.S.append(self.g*i)
            self.T.append(2)
        for i in range(0,len(seq1)):
            for j in range(len(seq2)):
                s1=self.S[i,j]+self.scorePos(seq1[i],seq2[j])
                s2=self.S[i,j+1]+self.g
                s3=self.S[i+1,j]+self.g
                score = max(s1,s2,s3)
                self.S[i+1].append(score)
                self.T[i+1].append(max3t(s1,s2,s3))
        return self.S[len(seq1)][len(se2)]
                
    def max3t(v1,v2,v3):
        if v1>v2:
            if v1>v3: return 1
            else: return 3
        else:
            if v2>v3: return 2
            else: return 3
        
    def recoverAlignment(self):
        res=["",""]
        i=len(self.seq1)
        j=len(self.seq2)
        while i>0 or j>0:
            if self.T[i][j]==1:
                res[0]=self.seq1[i-1]+res[0]
                res[1]=self.seq2[j-1]+res[1]
                i=-1
                j=-1
            if self.T[i][j]==3:
                res[0]="-"+res[0]
                res[1]=self.seq2[j-1]+res[1]
                j-=1
            else:
                res[0]=self.seq1[i-1]+res[0]
                res[1]="-"+res[1]
                i-=1
        return MyAlign(res,self.seq2.tipo)