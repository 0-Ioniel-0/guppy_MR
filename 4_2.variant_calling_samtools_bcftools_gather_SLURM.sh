#!/bin/bash -l

#SBATCH --time=10:00:00
#SBATCH --mem=60gb

PIC=/home/users/katarzynaburda/tools/picard/picard.jar
DIR=/home/users/katarzynaburda/MUTATION_RATE/SNP_CALLING/SAMTOOLS/final_T10-O

module load java8
module load bcftools/1.9

## What to combine?
t=$1

## Combine
java -Xmx60g -jar ${PIC} GatherVcfs \
TMP_DIR=/home/users/katarzynaburda/tmp \
R=/home/users/katarzynaburda/MUTATION_RATE/REF_GENOME/guppy.fa \
O=${DIR}/${t}/ALL.vcf.gz \
I=${DIR}/${t}/vcf_list.txt
