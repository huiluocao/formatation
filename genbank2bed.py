from Bio import SeqIO

with open('./PAO1.gb','r') as f:
    for rec in SeqIO.parse(f,'genbank'):
        print(rec.id)
        for feature in rec.features:
            #print(feature)
            if feature.type == 'CDS':
                locus_tag=(feature.qualifiers)['locus_tag']
                try:
                    gene=(feature.qualifiers)['gene']
                except:
                    gene=(feature.qualifiers)['locus_tag']
                try:
                    product=(feature.qualifiers)['product']
                except:
                    product=''
                try:
                    protein_id=(feature.qualifiers)['protein_id']
                except:
                    protein_id=""
                with open('PAO1.bed','a') as g:
                    g.write(locus_tag[0]+'\t'+gene[0]+'\t'+product[0]+'\t'+protein_id[0]+'\n')
