for file in os.listdir('./ref_genomes/zeta/fna/'):
    if file.endswith('16S_blastn.txt') and file.startswith('GCA'):
        sample=file[:15]
        genome=file[:-15]
        print(genome)
        print(sample)        
        with open('./ref_genomes/zeta/fna/%s'%file,'r') as f:
            for line in f.readlines():
                i=line.split('\t')
                contig=i[0]
                s=min(int(i[7]),int(i[6]))-1
                e=max(int(i[6]),int(i[7]))+1
                print(s,e)
                with open('./ref_genomes_16S_blastn.txt','a') as j:
                    j.write(sample+'\t'+line)
                with open('./ref_genomes/zeta/fna/%s'%genome,'r') as g:
                    for rec in SeqIO.parse(g,'fasta'):
                        if rec.id == contig:
                            rec.seq = rec.seq[s:int(e)]
                            rec.id = '%s_%s_%s_%s'%(sample,contig,s,e)
                            rec.description = ''
                            with open('16S_ref_genomes.fasta','a') as h:
                                SeqIO.write(rec,h,'fasta')
    elif file.endswith('16S_blastn.txt') and not file.startswith('GCA'):
        print(file)                              
        sample=file[:-19]
        genome=file[:-15]
        with open('./ref_genomes/zeta/fna/%s'%file,'r') as f:
            for line in f.readlines():
                i=line.split('\t')
                contig=i[0]
                s=min(int(i[7]),int(i[6]))-1
                e=max(int(i[6]),int(i[7]))+1
                print(s,e)
                with open('./ref_genomes_16S_blastn.txt','a') as j:
                    j.write(sample+'\t'+line)
                with open('./ref_genomes/zeta/fna/%s'%genome,'r') as g:
                    for rec in SeqIO.parse(g,'fasta'):
                        if rec.id == contig:
                            rec.seq = rec.seq[s:int(e)]
                            rec.id = '%s_%s_%s_%s'%(sample,contig,s,e)
                            rec.description = ''
                            with open('16S_ref_genomes.fasta','a') as h:
                                SeqIO.write(rec,h,'fasta')
