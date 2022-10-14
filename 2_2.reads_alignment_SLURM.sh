#!/bin/bash -l

#SBATCH -N 1
#SBATCH -n 10
#SBATCH --time=08:00:00
#SBATCH --mem=25gb

################# ALIGNMENT ################# 

module load samtools/1.6.0
module load bwa

# Input reads
IN=dir/to/TRIMMED
# Out BAMs
OUT=dir/to/BAMs
# Reference files. Index files should be mentioned only with directory and prefix, without .fasta !!!
R=dir/to/ref
# Temporary directory
T=dir/to/temp
# Sample name given by the outside loop. Each sample was run separately in the same time.
n=$1

# Aligning reads
bwa mem ${R} ${IN}/${n}_sample_1P.fastq.gz ${IN}/${n}_sample_2P.fastq.gz |\
samtools view -b -F 4 - > ${OUT}/${n}_sample.bam
# ^ option -F 4 makes sure these are only mapped reads.
