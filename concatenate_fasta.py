from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna

with open('./52genomes/5572B9_S1.fna','r') as f:
    seqs=[]
    for rec in SeqIO.parse(f,'fasta'):
        seqs.append(str(rec.seq))
    seq=''.join(seqs)
    rec= SeqRecord(Seq(seq,generic_dna),id='5572B9_S1',description='')
    print(rec.id)
    with open('./brig/5572B9_S1.fna','a') as g:
        SeqIO.write(rec,g,'fasta')
