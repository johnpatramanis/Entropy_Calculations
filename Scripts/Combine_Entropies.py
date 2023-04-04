import os
import random
import sys
import statistics

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
    PROTEIN_NAME=FILE.split('.entr')[0]
    ENTROPY_HERE=[]
    
    for line in PROTEIN_ENTROPY_FILE:
        line=line.strip()
        if (line!='') and (line!=' '):
            ENTROPY_HERE.append(float(line))
    
    
    PROTEIN_TO_ENTROPY[PROTEIN_NAME]=statistics.median(ENTROPY_HERE)


PROTEIN_TO_ENTROPY=sorted(PROTEIN_TO_ENTROPY.items(), key=lambda x:x[1])
print(PROTEIN_TO_ENTROPY)


for X in PROTEIN_TO_ENTROPY:
    PROTEIN=X[0]
    ENTROPY=X[1]
    print(F'{PROTEIN} : {ENTROPY}')
    Output_File.write(F'{PROTEIN} : {ENTROPY}\n')
    
    
    
LENGTH_FILE=open(sys.argv[3],'r') ### 'Entropies_Hominids/Protein_Lengths.txt'
LENGTH_FILE_PUT=open(Entropy_Folder+'/Lengths.txt','w') ### 'Entropies_Hominids/Lengths.txt'
LENGTHS=[]
for line in LENGTH_FILE:
    line=line.strip()
    if line!='':
        LENGTHS.append(int(line))

LENGTHS=sorted(list(set(LENGTHS)))
for k in LENGTHS:
    LENGTH_FILE_PUT.write(str(k)+'\n')