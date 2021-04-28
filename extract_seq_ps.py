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

                        
names={}
with open('seq.txt','r') as f:
    for line in f.readlines():
        i=line.split('\t')
        #print(i[6])
        a=(i[5]).strip()
        genus=(a.split(' '))[0]
        new_id='%s_%s-%s'%(i[0],i[1],i[2])
        #new_id='%s(%s_%s:%s)'%(a,i[0],i[1],i[2])
        old_id='%s_%s-%s:.'%(i[0],str(int(i[1])+1),i[2])
        names[old_id]=new_id
        with open('./seq_meta.txt','a') as g:
            g.write(new_id+'\t'+a+'\t'+genus+'\t'+i[3]+'\n')
            
            
with open('./seq.faa','r') as f:
    for rec in SeqIO.parse(f,'fasta'):
        #print(rec.id)
        i=names[('%s'%(rec.id))]
        rec.id=i
        print(rec.id)
        rec.description=''
        with open('./seq_clean.faa','a') as g:
            SeqIO.write(rec,g,'fasta')
