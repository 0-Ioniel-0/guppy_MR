#!/bin/bash

################# INDELs removal #################
# Since we are interested in point DNMs, indels can be removed.

TM=dir/to/temporary/files
input=$1

vcftools --gzvcf ${input} --remove-indels --recode --recode-INFO-all \
--temp ${TM} --out SNPs_only/${input}

# In this step, SNPs only VCF file is produced.