import pandas as pd
import os

blast_df_fil=pd.DataFrame()
for file in os.listdir('./'):
    if file.endswith('csv'):
        blast_df = pd.read_table(file,sep = ',', engine = 'python', header = None)
        #blast_df_fil = blast_df[blast_df.groupby([0])[11].transform(max)==blast_df[11]]
        blast_df_fil=blast_df_fil.append(blast_df.groupby([0]).first().reset_index())
print(blast_df_fil)
with open('../16S_batch2_ncbi_besthit.txt','w') as f:
    blast_df_fil.to_csv(f, header = True, index = False, sep = "\t"
