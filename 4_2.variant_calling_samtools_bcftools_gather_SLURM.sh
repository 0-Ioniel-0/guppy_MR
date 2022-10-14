#!/bin/bash -l

#SBATCH --time=10:00:00
#SBATCH --mem=60gb

PIC=dir/to/picard.jar
DIR=dir/to/raw_vcfs

module load java8
module load bcftools/1.9

## Combine
java -Xmx60g -jar ${PIC} GatherVcfs \
TMP_DIR=dir/to/temporary_files \
R=dir/to/ref/guppy.fa \
O=${DIR}/ALL.vcf.gz \
I=${DIR}/vcf_list.txt

# ^ It's a list of vcf files from all scaffolds with combined individuals.
