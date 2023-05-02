#!/bin/bash

################# VCFs intersection #################
# Here variants produced by GATK and samtools/bcftools; without indels and withough variants of missing parental genotypes,
# are intersected so that only ones shared by two methods are used in further steps. 

dir=/dir/to/vcfs

# -p is prefix for the output directory, inside this directory:
# 0001.vcf are variants private to GATK
# 0002.vcf are variants private to samtools/bcftools
# 0003.vcf are variants shared by GATK and samtools/bcftools in GATK file (THIS is the file we used in later steps)
# 0004.vcf are variants shared by GATK and samtools/bcftools in samtools/bcftools file
# These names are given by deafult, user has change the name of the wanted file themselves.
bcftools isec -O v -p ISEC \
${dir}/GATK_file.vcf.gz \
${dir}/samtools_bcftools_file.vcf.gz
