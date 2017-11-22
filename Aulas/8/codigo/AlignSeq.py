
from MyAlign import MyAlign
from MySeq import MySeq
from SubstMatrix import SubstMatrix

class AlignSeq:

    def __init__(self, sm, g):
        self.g = g
        self.sm = sm
        self.S = None
        self.T = None
        self.seq1 = None
        self.seq2 = None
        
    def scorePos (self, c1, c2):
        if c1 == "-" or c2=="-":
            return self.g
        else:
            return self.sm[c1,c2]
        
    def scoreAlin (self, alin):
        res = 0;
        for i in range(len(alin)):
            res += self.scorePos (alin[0][i], alin[1][i])
        return res
    
    def needlemanWunsch (self, seq1, seq2, ties = False):
        if (seq1.tipo != seq2.tipo): return None
        self.S = [[0]]
        self.T = [[0]]
        self.seq1 = seq1
        self.seq2 = seq2
        for j in range(1, len(seq2)+1):
            self.S[0].append(self.g * j)
            if ties: self.T[0].append([3])
            else: self.T[0].append(3)
        for i in range(1, len(seq1)+1):
            self.S.append([self.g * i])
            if ties: self.T.append([[2]])
            else: self.T.append([2])
        for i in range(0, len(seq1)):
            for j in range(len(seq2)):
                s1 = self.S[i][j] + self.scorePos (seq1[i], seq2[j])
                s2 = self.S[i][j+1] + self.g
                s3 = self.S[i+1][j] + self.g
                self.S[i+1].append(max(s1, s2, s3))
                if ties:
                    self.T[i+1].append(max3t_with_ties(s1, s2, s3))
                else:
                    self.T[i+1].append(max3t(s1, s2, s3))
        return self.S[len(seq1)][len(seq2)]
    
    def recoverAlignment (self):
        res = ["", ""]
        i = len(self.seq1)
        j = len(self.seq2)
        while i>0 or j>0:
            if self.T[i][j]==1:
                res[0] = self.seq1[i-1] + res[0]
                res[1] = self.seq2[j-1] + res[1]
                i -= 1
                j -= 1
            elif self.T[i][j] == 3:
                res[0] = "-" + res[0]
                res[1] = self.seq2[j-1] + res[1] 
                j -= 1
            else:
                res[0] = self.seq1[i-1] + res[0]
                res[1] = "-" + res[1]
                i -= 1
        return MyAlign(res, self.seq1.tipo)
    
    def recoverAlignment_with_ties (self):
        i = len(self.seq1)
        j = len(self.seq2)  
        alins = [["", "", i,j]]
        res = []
        while alins:
            al = alins.pop(0)
            i = al[2]
            j = al[3]
            if i==0 and j==0:
                res.append(al[:2])
            else:
                for t in self.T[i][j]:
                    p = []
                    if t==1:
                        p.append(self.seq1[i-1] + al[0])
                        p.append(self.seq2[j-1] + al[1])
                        p.append(i-1)
                        p.append(j-1)
                    elif t == 3:
                        p.append("-" + al[0])
                        p.append(self.seq2[j-1] + al[1])
                        p.append(i)
                        p.append(j-1)
                    else:
                        p.append(self.seq1[i-1] + al[0])
                        p.append("-" + al[1])
                        p.append(i-1)
                        p.append(j)
                    alins.append(p)
        return res
    
    
    def smithWaterman (self, seq1, seq2, ties = False):
        if (seq1.tipo != seq2.tipo): return None
        self.S = [[0]]
        self.T = [[0]]
        self.seq1 = seq1
        self.seq2 = seq2
        maxscore = 0
        for j in range(1, len(seq2)+1):
            self.S[0].append(0)
            if ties: self.T[0].append([0])
            else: self.T[0].append(0)
        for i in range(1, len(seq1)+1):
            self.S.append([0])
            if ties: self.T.append([[0]])
            else: self.T.append([0])
        for i in range(0, len(seq1)):
            for j in range(len(seq2)):
                s1 = self.S[i][j] + self.scorePos(seq1[i], seq2[j]) 
                s2 = self.S[i][j+1] + self.g
                s3 = self.S[i+1][j] + self.g
                b = max(s1, s2, s3)
                if b <= 0:
                    self.S[i+1].append(0)
                    self.T[i+1].append(0)
                else:
                    self.S[i+1].append(b)
                    if ties:
                        self.T[i+1].append(max3t_with_ties(s1, s2, s3))
                    else:
                        self.T[i+1].append(max3t(s1, s2, s3))
                    if b > maxscore: 
                        maxscore = b
        return maxscore

    def recoverLocalAlignment (self):
        res = ["", ""]
        maxscore = 0
        maxrow = 0
        maxcol = 0
        for i in range(1,len(self.S)):
            for j in range(1, len(self.S[i])):
                if self.S[i][j] > maxscore:
                    maxscore = self.S[i][j]
                    maxrow = i
                    maxcol = j
        i = maxrow
        j = maxcol
        while i>0 or j>0:
            if self.T[i][j]==1:
                res[0] = self.seq1[i-1] + res[0]
                res[1] = self.seq2[j-1] + res[1]
                i -= 1
                j -= 1
            elif self.T[i][j] == 3:
                res[0] = "-" + res[0];
                res[1] = self.seq2[j-1] + res[1]; 
                j -= 1
            elif self.T[i][j] == 2:
                res[0] = self.seq1[i-1] + res[0];
                res[1] = "-" + res[1]; 
                i -= 1
            else: break
        return MyAlign(res, self.seq1.tipo)


    def recoverAlignLocal_with_ties (self):
        maxval = self.S[0][0]
        maxtups = []
        for i in range(0,len(self.S)):
            for j in range(0, len(self.S[i])):
                if self.S[i][j] > maxval:
                    maxval = self.S[i][j]
                    maxtups = [(i,j)]
                elif self.S[i][j] == maxval:
                    maxtups.append((i,j))
        alins = []
        for (i,j) in maxtups:
            alins.append(["", "", i,j])        
        res = []
        while alins:
            al = alins.pop(0)
            i = al[2]
            j = al[3]   
            if (i==0 and j==0) or (0 in self.T[i][j]):
                res.append(al[:2])
            else:
                for t in self.T[i][j]:
                    p = []
                    if t==1:
                        p.append(self.seq1[i-1] + al[0])
                        p.append(self.seq2[j-1] + al[1])
                        p.append(i-1)
                        p.append(j-1)
                    elif t == 3:
                        p.append("-" + al[0])
                        p.append(self.seq2[j-1] + al[1])
                        p.append(i)
                        p.append(j-1)
                    else:
                        p.append(self.seq1[i-1] + al[0])
                        p.append("-" + al[1])
                        p.append(i-1)
                        p.append(j)
                    alins.append(p)
        return res

    
def max3t (v1, v2, v3):
    if v1 > v2:
        if v1 > v3: return 1
        else: return 3
    else:
        if v2 > v3: return 2
        else: return 3

def max3t_with_ties(v1, v2, v3):
    if v1 > v2:
        if v1 > v3: 
            return [1]
        elif v1 == v3:
            return [1,3]
        else:
            return [3]
    elif v1 == v2:
        if v1 > v3: 
            return [1,2]
        elif v1 == v3:
            return [1,2,3]
        else:
            return [3]
    else:
        if v2 > v3: return [2]
        elif v2 == v3:
            return [2,3]
        else: return [3]

def printMat (mat):
    for i in range(0, len(mat)):
        print(mat[i])

def lcs (seq1, seq2):
    sm = SubstMatrix()
    sm.createFromMatchPars(1,0, seq1.alfabeto())
    aseq = AlignSeq(sm, 0)
    aseq.needlemanWunsch(seq1, seq2)
    alin = aseq.recoverAlignment ()
    sizeal = len(alin[0])
    lcs = ""
    for i in range(sizeal):
        if alin[0][i] != "-" and alin[0][i] == alin[1][i]:
            lcs += alin[0][i]
    return lcs        

    
def edit_distance(seq1, seq2):
    sm = SubstMatrix()
    sm.createFromMatchPars(0,-1,seq1.alfabeto())
    aseq = AlignSeq(sm, -1)
    sc = aseq.needlemanWunsch(seq1, seq2)
    return -sc
    
    
    
#### TESTS #####

def test1():
    #seq1 = MySeq("NCRD","protein")
    #seq2 = MySeq("CRNC","protein")
    seq1 = MySeq("DRCN","protein")
    seq2 = MySeq("NCRC","protein")
    sm = SubstMatrix()
    sm.loadFromFile("blosum62.mat", "\t")
    alin = AlignSeq(sm, -3)
    print(alin.needlemanWunsch(seq1, seq2))
    printMat(alin.S)
    print()
    printMat(alin.T)
    print(alin.recoverAlignment())


def test2():
    seq1 = MySeq("ATGATATGATGATT")
    seq2 = MySeq("GATGAATAGATGTGT")
    sm = SubstMatrix()
    sm.createFromMatchPars(3, -1, "ACGT")
    alin = AlignSeq(sm, -3)
    print(alin.smithWaterman(seq1, seq2))
    printMat(alin.S)
    print(alin.recoverLocalAlignment())


def testTies():
    sm = SubstMatrix()
    sm.loadFromFile("blosum62.mat", "\t")
    alin = AlignSeq(sm, -1)
    
    seq1 = MySeq("GKYESVI")
    seq2 = MySeq("KYVSSWI")
    sc = alin.needlemanWunsch(seq1, seq2, True)
    printMat(alin.S)
    printMat(alin.T)
    print("Melhor score do alinhamento otimo global:", sc)
    alins = alin.recoverAlignment_with_ties()
    for a in alins: print(a)
    
    alin.g = -3
    sc = alin.smithWaterman(seq1, seq2, True)
    print("Melhor score do alinhamento otimo local: " , sc)

    alinsL = alin.recoverAlignLocal_with_ties()
    for a in alinsL: print(a)


def testLCS():
    s1 = MySeq("ATTAGCT")
    s2 = MySeq("ATAAGCT")
    print(lcs(s1,s2))


def testED():
    s1 = MySeq("ATTAGCT")
    s2 = MySeq("ATTAAAGCT")
    print(edit_distance(s1,s2))



if __name__ == "__main__":   
    print("Teste 1")
    test1()
#    print("Teste 2")
#    test2()
#    print("Teste 3")
#    testLCS()
#    print("Teste 4")
#    testED()
#    print("Teste 5")
#    testTies()

