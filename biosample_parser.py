with open('./114biosample_result.txt','r') as f:
    chunks=(f.read()).split('\n\n')
    for chunk in chunks:
        for line in chunk.split('\n'):
            if 'Identifiers' in line:
                a=line
            if 'collection date' in line:
                d=line
        print(a,d)
