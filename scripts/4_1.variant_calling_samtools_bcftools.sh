#!/bin/bash

################# samtools/bcftools variant calling #################
# Since piling up requires a lot of time and resources, it is recommended to do it parallelly per chromosome.

# All bams (individuals) must be listed in following list to be piled up together#
BAMLIST=dir/to/bams/list.txt
GENOME=dir/to/REF_GENOME/genome.fasta
# List of genomic scaffolds (chromosomes).
chromsome=$1
OUT=dir/to/output/

# Samtools gathers all individuals and extract just one region at time. Remember to add -t DP,ADF,ADR #
# -r gives samtools chromosome to operate on. Bgzip compresses the file and tabix indexes vcf.gz file.
samtools mpileup -R -t DP,ADF,ADR -vuf $GENOME -b $BAMLIST -r "${chromsome}" -o ${OUT}/gvcf/tmp.${chromsome}.raw.vcf
bgzip ${OUT}/gvcf/tmp.${chromsome}.raw.vcf && tabix ${OUT}/gvcf/tmp.${chromsome}.raw.vcf.gz

# Bcftools calls variants from the genomic VCF. Remember to add -f GQ #
bcftools call -f GQ -vmO v -o ${OUT}/vcf/${chromsome}.SNPs.vcf ${OUT}/gvcf/tmp.${chromsome}.raw.vcf.gz
bgzip ${OUT}/vcf/tmp.${chromsome}.SNPs.vcf && tabix ${OUT}/vcf/tmp.${chromsome}.SNPs.vcf.gz

# The VCF for one chromosome in all individuals has been produced.
