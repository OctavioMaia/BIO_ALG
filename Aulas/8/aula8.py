from Bio import SeqIO
from Bio import AlignIO
from Bio import pairwise2


""" Ex1 """

records = SeqIO.convert("PF05371_seed.sth","stockholm","PF05371.fasta","fasta")
records2 = SeqIO.convert("PF05371_seed.sth","stockholm","PF05371.aln","clustal")



print("============  Ex2  ============")
print("\n------------  1)  -------------")
alignmentA = AlignIO.read("alpha.faa", "fasta")
alignmentB = AlignIO.read("beta.faa", "fasta")

print (alignmentA)
print ("\n")
print (alignmentB)

print("\n------------  2)  -------------")

alignments = pairwise2.align.globalxx("AAA", "ABC")
print(alignments)

print("\n------------  3)  -------------")

print("\n------------  4)  -------------")

print("\n------------  5)  -------------")

print("\n------------  6)  -------------")