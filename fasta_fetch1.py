import sys
from Bio import SeqIO

FastaFile = open('farm_AR_mix.faa', 'rU')



with open('list_1.txt','r') as f:
    list_id = []
    lines = f.readlines()
    for line in lines:
##        print(line)
        list_id.append(line.strip())
with open("farm_AR1.faa","w") as g:
    for rec in SeqIO.parse(FastaFile, 'fasta'):
        name = rec.id
        print(name)
##        for seq_id in list_id:
        if name in list_id:
            SeqIO.write([rec], g, "fasta")
            with open("seq_list_1.txt","a") as h:
                h.write(name+"\n")
                


FastaFile.close()
