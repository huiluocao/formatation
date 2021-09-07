with open('./114biosample_result.txt','r') as f:
    chunks=(f.read()).split('\n\n')
    for chunk in chunks:
        for line in chunk.split('\n'):
            if 'Identifiers' in line:
                a=line
            if 'collection date' in line:
                d=line
        print(a,d)
        
        
with open('./biosample_result.txt','r') as f:
    chunks=(f.read()).split('\n\n')
    for chunk in chunks:
        #print(chunk)
        d=''
        for line in chunk.split('\n'):
            line=line.strip()
            try:
                if 'Identifiers' in line:
                    a=line
            except:
                a='n/a'
            try: 
                if 'geographic location' in line:
                    d=line
            except:
                d='n/a'
        with open('./biosample_location.txt','a') as g:
            g.write(a+'\t'+d+'\n')
