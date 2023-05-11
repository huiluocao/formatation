with open('./A21Q178.gbk','r') as f:
    for rec in SeqIO.parse(f,'gb'):
        if rec.id =='1':
            print(rec.id)
            ice_cfr=rec[2359506:2559602]
            #rec.id='ice_cfr'
            with open('./A21Q178_cfr_ice.gbk','a') as g:
                SeqIO.write(ice_cfr,g,'gb')
            with open('./A21Q178_cfr_ice.fasta','a') as h:
                SeqIO.write(ice_cfr,h,'fasta')
