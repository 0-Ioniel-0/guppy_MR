#!/bin/bash -l

################# GATK VCF calling #################
# gVCF produced in previous step are now used for joined calling of a VCF file.

GATK=dir/to/gatk
REF=dir/to/REF_GENOME/guppy.fa
family_name=$1

gatk --java-options "-Xmx60g" GenotypeGVCFs \
-R ${REF} -V gvcfs/${family_name}_family_final.g.vcf.gz -O vcfs/${family_name}_family_final.vcf.gz

# In this step, VCF file for a given family is produced.
