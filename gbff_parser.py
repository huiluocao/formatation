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


for file in os.listdir('./'):
    if file.endswith('gbff'):
        GCA=file[0:15]
        print(GCA)
        with open(file,'r') as f:
            recs=[]
            for rec in SeqIO.parse(f,'genbank'):
                recs.append(rec)
            rec=recs[0]
            orga = rec.annotations['organism']
            try:
                family = rec.annotations['taxonomy'][4]
            except:
                family = 'n/a'
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
            with open('../193gca_info.txt','a') as g:
                g.write('\t'.join([GCA,orga,family,strain,acc,biop,bios,ref,des,source,country,date])+'\n')
                    

                    
                    
                    
###### wrong code:
with open('./989biosample_result-2.txt', 'r') as f:
    txt=f.read()
    chunks = txt.split('\n\n')
    print(len(chunks))
    for chunk in chunks:
        info = []
        for line in chunk.split('\n'):
            try:
                if 'Identifiers' in line:
                    bios=(line.split(';')[0]).split(':')[2]
                    sample_id = (line.split(';')[1]).split(':')[1]
            except:
                    sample_id = 'n/a'
            try:
                if '/strain' in line:
                    strain=line.split('"')[1]
            except:
                strain='n/a'
            try:
                if '/host' in line:
                    host = line.split('"')[1]
            except:
                host = 'n/a'
            try:
                if '/isolation source' in line:
                    source = line.split('"')[1]
            except:
                source = "n/a"
            try:
                '/sequence_type' in line
                sequence_type = line.split('"')[1]
            except:
                sequence_type = 'n/a'
        print(bios,sample_id,strain,host,source,sequence_type)
        #with open('./989biosample_clean.txt','a') as g:
        #    g.write('\t'.join([bios,sample_id,strain,host,source,sequence_type])+'\n')
