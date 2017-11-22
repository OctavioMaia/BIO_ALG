class MySeq:

    def __init__(self, seq, tipo="dna"):
        self.seq = seq.upper()
        self.tipo = tipo

    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, n):
        return self.seq[n]

    def __getslice__(self, i, j):
        return self.seq[i:j]

    def __str__(self):
        return self.tipo + ":" + self.seq

    def printseq(self):
        print(self.seq)
    
    def alfabeto(self):
        if (self.tipo=="dna"): return "ACGT"
        elif (self.tipo=="rna"): return "ACGU"
        elif (self.tipo=="protein"): return "ACDEFGHIKLMNPQRSTVWY"
        else: return None
    
    def valida(self):
        alf = self.alfabeto()
        res = True
        i = 0
        while i < len(self.seq) and res:
            if self.seq[i] not in alf: 
                res = False
            else: i += 1
        return res 

    
    def transcricao (self):
        if (self.tipo == "dna"):
            return MySeq(self.seq.upper().replace("T","U"), "rna")
        else:
            return None
        
    def compInverso(self):
        if (self.tipo != "dna"): return None
        comp = ""
        for c in self.seq.upper():
            if (c == 'A'):
                comp = "T" + comp 
            elif (c == "T"): 
                comp = "A" + comp 
            elif (c == "G"): 
                comp = "C" + comp
            elif (c== "C"): 
                comp = "G" + comp
        return MySeq(comp)

    def traduzSeq (self, iniPos= 0):
        if (self.tipo != "dna"): return None
        seqM = self.seq.upper()
        seqAA = ""
        for pos in range(iniPos,len(seqM)-2, 3):
            cod = seqM[pos:pos+3]
            seqAA += self.traduzCodao(cod)
        return MySeq(seqAA, "protein")

    def orfs (self):
        """
        Determinar todas as ORFS assumindo que self e' uma seq de DNA
        """

    def traduzCodao (self, cod):
        tc = {"GCT":"A", "GCC":"A", "GCA":"A", "GCC":"A", "TGT":"C", "TGC":"C",
      "GAT":"D", "GAC":"D","GAA":"E", "GAG":"E", "TTT":"F", "TTC":"F",
      "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G","CAT":"H", "CAC":"H",
      "ATA":"I", "ATT":"I", "ATC":"I",
      "AAA":"K", "AAG":"K",
      "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
      "ATG":"M", "AAT":"N", "AAC":"N",
      "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
      "CAA":"Q", "CAG":"Q",
      "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
      "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
      "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
      "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
      "TGG":"W",
      "TAT":"Y", "TAC":"Y",
      "TAA":"_", "TAG":"_", "TGA":"_"}
        if cod in tc:
            aa = tc[cod]
        else: aa = "X" # errors marked with X
        return aa


    def maiorProteina (self):
        """
        Determinar a maior proteina numa seq de AAs
        """
    
    def todasProteinas(self):
        """
        Determinar todas as proteinas numa seq de AAs
        """
        

    
    def maiorProteinaORFs (self):
        """
        Determinar maior proteina de todas as ORFs
        """

def readFastaToDict(file_name):
    """
    # reads a fasta file an returns the sequences in a dictionary
    # keys are the sequence name and values are the sequence string.
    # Note that the name of the sequence is defined as the string after 
    # the symbol > and goes until the first space    
    """
    fh = open(file_name, "r")
    seq = ""
    seq_dict = {}
    count = 0
    for line in fh.readlines():
        if line.count(">") > 0:
            seq_id = line[1:].split()[0]
        if line.count(">") == 0 :
            if seq_id in seq_dict:
                seq_dict[seq_id] += line.strip()
            else:
                seq_dict[seq_id] = line.strip()
           
    return (seq_dict)

# teste
def teste():
    seq_dict = readFastaToDict("HBA.DNA.fasta")
    seq_dna = seq_dict["HBA1"]
    s1 = MySeq(seq_dna)
    s1.printseq()


    
    if s1.valida():
        # a medida que vai implementando o codigo acima teste as funcionalidades abaixo
        print("Sequencia valida")
        print("Transcricao: ")
        # codigo para transcricao de s1, imprima resultado
        print("Complemento inverso:") 
        # codigo para complemento inverso de s1, imprima resultado
        print("Traducao: ") 
        # codigo para traducao de s1, imprima resultado
        print("ORFs:")
        # codigo para imprimir todos os ORFs
        print("Maior proteina nas ORFs:")
        # codigo para imprimir a maior sequencia entre todos os ORFs
    else:
        print("Sequencia invalida")

if __name__ == "__main__": 
    teste()
