#!/bin/bash

module load bcftools/1.9

dir=/dir/to/vcfs

# -p is prefix for the output directory, inside this directory:
# 0001.vcf is variants private to Gatk
# 0002.vcf is variants private to Samtools/bcftools
# 0003.vcf is variants shared by Gatk and Sam/bcf in Gatk file
bcftools isec -O v -p ISEC \
# GATK file
${dir}/G_7.vcf.gz \
# Samtools/bcftools file
${dir}/S_7.vcf.gz
