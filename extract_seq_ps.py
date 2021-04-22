with open('./16S_ref_1.list','r') as f:
    for line in f.readlines():
        line=line.strip()
        i=line.split('.')
        s= min([int(i[1]),int(i[2])])
        e= max([int(i[1]),int(i[2])])
        with open('./16S_ref.fasta','r') as g:
            for rec in SeqIO.parse(g,'fasta'):
                if (rec.id)[:-2] == i[0]:
                    print(rec.id)
                    rec.seq = (rec.seq)[(s-1):e]
                    with open('./16S_ref_clean.fasta','a') as h:
                        SeqIO.write(rec,h,'fasta')
