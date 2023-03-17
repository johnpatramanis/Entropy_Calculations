import os
import random
import sys

from Bio import SeqIO


Entropy_Folder=sys.argv[1]
OF=sys.argv[2]
Output_File=open(OF,'w')

FILES=os.listdir(Entropy_Folder)
FILES=[x for x in FILES if '.entr' in x]
PROTEIN_TO_ENTROPY={}


for FILE in FILES:
    PROTEIN_NAME=FILE.split('.entr')[0]
    PROTEIN_ENTROPY_FILE=open(F'{Entropy_Folder}/{FILE}','r')
    
    ENTROPY_HERE=[]
    
    for line in PROTEIN_ENTROPY_FILE:
        line=line.strip()
        if (line!='') and (line!=' '):
            ENTROPY_HERE.append(float(line))
    
    
    PROTEIN_TO_ENTROPY[FILE]=(sum(ENTROPY_HERE)/len(ENTROPY_HERE))


PROTEIN_TO_ENTROPY=sorted(PROTEIN_TO_ENTROPY.items(), key=lambda x:x[1])
print(PROTEIN_TO_ENTROPY)


for X in PROTEIN_TO_ENTROPY:
    PROTEIN=X[0]
    ENTROPY=X[1]
    print(F'{PROTEIN} : {ENTROPY}')