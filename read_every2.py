with open('./swine_unmapped_qc.txt','r') as f:
    for line1,line2 in itertools.zip_longest(*[f]*2):
        line1=line1.strip()
        line2=line2.strip()
        with open('./swine_unmapped_qc_raw.txt','a') as g:
            g.write(line1+'\t'+line2+'\n')
            
            
with open('./chicken_qc.txt') as f:
    for line1, line2 in zip(f, f):
        print(line1, line2)  
