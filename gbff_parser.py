for file in os.listdir('./'):
    if file.endswith('gbff'):
        GCA=file[0:15]
        print(GCA)
        with open(file,'r') as f:
            for rec in SeqIO.parse(f,'genbank'):
                orga = rec.annotations['organism']
                try:
                    strain = ((rec.features[0]).qualifiers['strain'])[0]
                except:
                    strain = 'n/a'
                acc = (rec.annotations['accessions'])[0]
                biop = ((rec.dbxrefs[0]).split(':'))[1]
                bios = ((rec.dbxrefs[1]).split(':'))[1]
                ref = ((rec.annotations['references'])[0]).title
                des = rec.description
                try:
                    source = ((rec.features[0]).qualifiers['isolation_source'])[0]
                except:
                    source = 'n/a'
                try:
                    country = ((rec.features[0]).qualifiers['country'])[0]
                except:
                    country = 'n/a'
                try:
                    date = ((rec.features[0]).qualifiers['collection_date'])[0]
                except:
                    date = 'n/a'
                with open('../989gca_info.txt','a') as g:
                    g.write('\t'.join([GCA,orga,strain,acc,biop,bios,ref,des,source,country,date])+'\n')
