def readFasta(file):
    f = open(file,"r")
    id=""
    seq=""
    for line in f:
        if line.startswith(">"):
            id = line[1:]
        else:
            seq+=line
    f.close()
    return (id,seq)

print(readFasta("query1.fasta"))