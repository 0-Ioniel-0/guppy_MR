
################# ALIGNMENT ################# 

module load samtools/1.6.0
module load bwa

# Input reads
OUT=dir/to/TRIMMED
# Out BAMs
OUT_B=dir/to/BAMs
# Reference files. Index files should be mentioned only with directory and prefix, without .fasta !!!
R=dir/to/ref
# Temporary directory
T=dir/to/temp
