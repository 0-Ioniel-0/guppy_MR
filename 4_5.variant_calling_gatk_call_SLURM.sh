#!/bin/bash -l

#SBATCH --mem=60g

module load java8

gatk --java-options "-Xmx60g" GenotypeGVCFs \
-R reference.fa -V merged.g.vcf.gz -O final.vcf.gz
