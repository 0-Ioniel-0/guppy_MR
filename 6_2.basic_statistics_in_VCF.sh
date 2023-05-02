#!/bin/bash

################# basic statistics in VCF file #################
# We checked basic statistics like nucleotide diversity, TS/TV, ROH and Heterozygosity in VCF files.
# First three were done with vcftools, heterozygosity was checked using python script.

input=family.vcf

# Stats with vcftools
vcftools --vcf ${input} --out ${input}_pi.txt --window-pi 75000
vcftools --vcf ${input} --out ${input}_tstv.txt --TsTv-summary
vcftools --vcf ${input} --out ${input}_roh.txt --LROH

# Heteryzgosity with python script.
# Note that we had 12 individuals in family file. If one has less, one should trim the python script in appropriate places.
python heterozygosity_assesment.py ${input} 