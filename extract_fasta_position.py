#!/usr/bin/env python
# extract fasta sequence by their position
# Downloaded from http://www.bioinformatics-made-simple.com/2013/10/actually-i-have-hundreds-of-protein.html
import sys
import re

##FASTA= sys.argv[1]
##BED= sys.argv[2]

FASTA= 'C:/Users/Huiluo/Desktop/HKU-microbiology/pneumococcus/genomes/cps_sp3/hku_s3_cps/hku_sp3.fna'
BED= 'C:/Users/Huiluo/Desktop/HKU-microbiology/list1.txt'
output = 'C:/Users/Huiluo/Desktop/HKU-microbiology/ERS508537_contig000008.fasta'

fasta= open(FASTA, 'U')
fasta_dict= {}
for line in fasta:
    line= line.strip()
    if line == '':
        continue
    if line.startswith('>'):
        seqname= line.lstrip('>')
        seqname= re.sub('\s.*', '', seqname)
##        print seqname
        fasta_dict[seqname]= ''
    else:
        fasta_dict[seqname] += line
fasta.close()

output_fasta = open(output,'w')
    
bed= open(BED, 'U')
for line in bed:
    line= line.strip().split('\t')
    outname= line[0] + ':' + line[1] + '-' + line[2] + '\n'
    header = '>'+ outname
    output_fasta.write(header)
    s= int(line[1])
    e= int(line[2])
##    print fasta_dict.keys()
    seq = fasta_dict[line[0]][s:e]
##    print seq
    output_fasta.write(seq+'\n')
    
bed.close()
output_fasta.close()
sys.exit()
