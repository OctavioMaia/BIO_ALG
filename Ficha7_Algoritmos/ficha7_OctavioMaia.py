from Bio import SeqIO
from Bio.Data import CodonTable
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#-------------PARTE 1-------------
#1
print("\nExercicio 1")
seq_in=SeqIO.read("sequence.fasta","fasta")
print(seq_in)

#2
print("\nExercicio 2")
fasta=seq_in.seq
count=len(fasta)
print("Nº de PB: %d" %count)
g=(fasta.count("G")*100)/count
c=(fasta.count("C")*100)/count
print("C=%.2f%% G=%.2f%%" %(c,g))

#3
print("\nExercicio 3")
fasta_inverso=fasta.reverse_complement()
print("Inverso: " + fasta_inverso)

#4
print("\nExercicio 4")
trans=fasta_inverso.transcribe()
print("Transcricao: " + trans)

#5
print("\nExercicio 5")
pos=fasta.find("GTG")
print("Posicao codão start: %d" %pos)

#6
print("\nExercicio 6")
seq=fasta[339:342]
found=seq.find("TAA")
comp=len(fasta[pos:342])

if found:
    print("Existe o codão TAA na sequencia")
else:
    print ("Não existe o codão TAA na sequencia")
if comp%3==0:
    print("Tamanho válido")
else:
    print("Tamanho inválido")

#7
print("\nExercicio 7")
seq2=fasta[pos:342]
comp2=len(fasta[pos:342])
table=CodonTable.unambiguous_dna_by_name["Bacterial"]
translate=seq2.translate(table="Bacterial")
translate_cds=seq2.translate(table="Bacterial",cds=True)

print("CDS==false")
if (len(seq2)/(len(translate)+1))==3:
    print("Numero de aminoácidos: %d" %((comp2/3)-1))
    print("Aminoacido inicial: %s" % translate[0])
    print('Comprimento da proteína correto')
else:
    print('Comprimento da proteína incorreto')

print("\nCDS==true")
if (len(seq2)/(len(translate_cds)+1))==3:
    print("Numero de aminoácidos: %d" %((comp2/3)-1))
    print("Aminoacido inicial: %s" % translate_cds[0])
    print('Comprimento da proteína correto')
else:
    print('Comprimento da proteína incorreto')
    
#-------------PARTE 2-------------
print("\nExercicio 1")
seq_in2=SeqIO.read("sequence.gb","gb")
print("ID: %s" %seq_in2.id)
print("Descrição: %s" %seq_in2.description)
print("Nome: %s" %seq_in2.name)
print("Num PB: %d" %len(seq_in2.seq))

#2
print("\nExercicio 2")
print("\nOrganismo: %s" %seq_in2.annotations["organism"])
print("\nTaxonomia: %s" %seq_in2.annotations["taxonomy"])

#3
print("\nExercicio 3")
for i in seq_in2.features:
    print('\nFeature do tipo:',i.type)
    print('Localização:',i.location)

#4
print("\nExercicio 4")
length=len(seq_in2.features)
for i in range (length):
    if seq_in2.features[i].type == "CDS":
        print('\nProteina:',seq_in2.features[i].qualifiers['protein_id'])
        print('Funcao:',seq_in2.features[i].qualifiers['product'])

#5
print("\nExercicio 5")
cadeia_1 = []
cadeia_2 = []

for feature in seq_in2.features:
    if feature.type.upper() == "GENE":
        if feature.location.strand > 0:
            cadeia_1.append(feature.qualifiers["gene"][0])
        else:
            cadeia_2.append(feature.qualifiers["gene"][0])
print("Cadeia 1: ",cadeia_1)
print("Cadeia 2: ",cadeia_2)

#6
print("\nExercicio 6")
flag = SeqIO.write(seq_in2,"ex6.fasta","fasta")
if(flag):
    print("Sucesso na conversão para fasta")
else:
    print("Insucesso na conversão para fasta")

#-------------PARTE 3-------------

#1
print("\nExercicio 1")
seq_in3 = SeqIO.read("O14727.fasta", "fasta")
fasta2=seq_in3.seq
print("Numero de aminoacidos:", len(fasta2))

#2
print("\nExercicio 2")
result=NCBIWWW.qblast("blastp","swissprot",seq_in3.format("fasta"))
file=open("similar.xml","w")
file.write(result.read())
file.close()
result.close()

#3
print("\nExercicio 3")
result=open("similar.xml")
blast=NCBIXML.read(result)
print("DB: ",blast.database)
print("Matrix: ",blast.matrix)
print("Gaps:",blast.gap_penalties)

#4
print("\nExercicio 4")
for entry in blast.alignments:
    print("Accession:",entry.accession)
    print("Comprimento:", entry.length)
    print("E-Value:", entry.hsps[0].expect)

      
#5
print("\nExercicio 5")
result2=NCBIWWW.qblast("blastp","swissprot",seq_in3.format("fasta"), entrez_query="Saccharomyces cerevisiae[organism]")
file2=open("similar2.xml","w")
file2.write(result2.read())
file2.close()
result2.close()

#6
print("\nExercicio 6")
file = open("similar2.xml")
blast2=NCBIXML.read(file)
entry=blast2.alignments[0]
print("Accession:",entry.accession)
print("Descricao:", entry.hit_def)
print("Numero de HSPs:", len(entry.hsps))

for hsp in entry.hsps:
    print("\nTamanho do alinhamento:", hsp.align_length)
    print("Inicio HSP query:", hsp.query_start)
    print("Inicio HSP subject:", hsp.sbjct_start)

#6
"""
Primeiramente, acederia ao registo uniprot procurando pelo gene "APAF" do
organismo "S. Cerevisiae". A partir daí descarregaria o ficheiro ".fasta"
correspondente.

De seguida converteríamos o ficheiro XML da pergunta 5 para FASTA e
utilizaríamos a ferramenta online BLAST(N) para comparar ambas as sequências.

Se se encontrassem alinhamentos entre as duas sequências e pela análise do
output final deste programa, era possível concluir se existia ou não homologia.
"""