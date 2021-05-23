l=[]
for i in range(1,10):
    l.append(i*10)
print(l)





l=[]
for i in range(1,10):
    l.append(i*i*i)
print(l)


l=['Adobe','Bingo','coy','Daniel','Evan']
res=[]
for i in l:
    res.append(i.title()+"is awesome!")
for i in res:
    print(i)
    
    
    dna='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
a=0
c=0
t=0
g=0
for i in dna:
    if(i=='A'):
        a=a+1
    elif(i=='G'):
        g=g+1
    elif(i=='C'):
        c=c+1
    elif(i=='T'):
        t=t+1
print("A=%d G=%d C=%d T=%d",a,g,c,t)


