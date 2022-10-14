#!/bin/bash -l

#SBATCH --mem=60g

D=/home/users/katarzynaburda/MUTATION_RATE/SNP_CALLING/GATK
R=/home/users/katarzynaburda/MUTATION_RATE/REF_GENOME/guppy.fna
G=/home/users/katarzynaburda/tools/gatk-4.1.4.1/gatk

module load java8

${G} --java-options "-Xmx60g" GenotypeGVCFs \
-R ${R} -V ${D}/ALL_final.g.vcf.gz -O ${D}/final/ALL_final.vcf.gz
