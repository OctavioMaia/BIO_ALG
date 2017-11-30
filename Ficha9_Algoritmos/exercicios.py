from Bio.Align import MultipleSeqAlignment 
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio import Phylo
#1
print("#1")
alignments = AlignIO.parse("p3.clustal", "clustal")
als = []
for al in alignments:
	als.append(al)
	print (str(al))

#2
print("#2")
for al in als:
	a = AlignInfo.SummaryInfo(al)
	print(str(a.dumb_consensus()))

#3
print("#3")
conserved = []
 
alignments = AlignIO.parse("p3.clustal", "clustal")
for alignment in alignments:
    matrix = [list(line) for line in alignment]
    transpose = []
    for line_nr, line in enumerate(zip(*matrix)):
        transpose.append(line)
        if all(x == line[0] for x in line):
            conserved.append(line_nr)
 
    print("No alinhamento, as seguintes colunas conservam o alinhamento:")
    print(conserved)
    percent = len(conserved) / len(transpose)
    print("A sua percentagem de ocorrencia é: " + str(percent))

#4
print("#4")
zones = [[]]
i = 0
j = 0
 
for c in conserved:
    if i == c:
        zones[j].append(i)
        i += 1
    else:
        i += 2
        j += 1
        zones.append([c])
 
most_conserved = max(zones, key=len)
print("A zona de alinhamento mais conservada é a região: ")
print("[" + str(most_conserved[0]) + " - " + str(most_conserved[-1]) + "]: " + str(most_conserved))

#5
print("#5")
tree = Phylo.read('tree.ph', 'newick')
Phylo.draw_ascii(tree)