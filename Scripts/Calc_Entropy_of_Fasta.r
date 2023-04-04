### install.packages("bio3d", dependencies=TRUE)
### http://thegrantlab.org/bio3d/reference/entropy.html
### Run like this: R Calc_Entropy_of_Fasta.r A1BG_PROT_REFERENCE.fa PER_PROTEIN Entropies_Hominids
args = commandArgs(trailingOnly=TRUE)
library('bio3d')

##### load file and names
Directory_Path <- args[2]
Fasta_alignment <- read.fasta(paste(args[2], args[1], sep="/"),rm.dup = FALSE)  ##### should not contain '?', replace with '-'
Name_of_Protein<- gsub('_PROT_REFERENCE.fa','',args[1])




### Output file
OUTPUT_FODLER_FULL_PATH <- args[3]
OUTPUT_FODLER_FULL_PATH <- paste(OUTPUT_FODLER_FULL_PATH,Name_of_Protein,sep='/')
OUTPUT_FODLER_FULL_PATH <- paste(OUTPUT_FODLER_FULL_PATH,'.entr',sep='')

OUTPUT_LENGTH <- args[3]
OUTPUT_LENGTH <- paste(OUTPUT_LENGTH,'Protein_Lengths.txt',sep='/')



#### 
print(Name_of_Protein)

###
##### Clean up columns with missing value
GAPS=which(Fasta_alignment$ali=='-',arr.ind=TRUE) ## Find columns with gaps
if (length(GAPS[,2])>0){
	Fasta_alignment$ali <- Fasta_alignment$ali[,-(GAPS[,2])] ## Remove them from alignment, use the rest for entropy
	}


####
#### Calculate Entropy etc
if (length(Fasta_alignment$ali)>0){

	Entropy_Metrics <- entropy(Fasta_alignment)
	Entropy_Pure <- Entropy_Metrics$H      ### Standard Entropy Score for a 22-letter alpahabet
	Entropy_Norm <- Entropy_Metrics$H.norm ### Normalised entropy score ## seems to be reverse

	## Get Average Metrics
	Protein_Mean_Entropy<- ( sum(Entropy_Pure) / length(Entropy_Pure) )
	Protein_Mean_Entropy_Normalised<- ( sum(Entropy_Norm) / length(Entropy_Norm) )


	# ConsensusS <- consensus(Fasta_alignment)
	# ConsensusSequence <- ConsensusS$seq #### The consensus Sequence if we want it


	OUTPUT=paste(Protein_Mean_Entropy,'\n',sep='')
	# OUTPUT=paste(Protein_Mean_Entropy)
	LENGTH=length(Fasta_alignment$ali)
	LENGTH=paste(LENGTH,'\n',sep='')
	
	##### Output
	write(OUTPUT, file=OUTPUT_FODLER_FULL_PATH,append = TRUE)
	write(LENGTH, file=OUTPUT_LENGTH,append = TRUE)
}