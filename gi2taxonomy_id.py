from Bio import Entrez

with open('feature_nt_blastn1.txt','r') as f:
    for line in f.readlines():
        accession_id = line.split('\t')[1]
        handle = Entrez.efetch(db="nuccore", id=accession_id, rettype="gb", retmode="xml")
        record = Entrez.read(handle)
        handle.close()
        with open('feature_nt_taxonomy.txt','a') as g:
            g.write(record[0]["GBSeq_taxonomy"]+'\t'+line)
