#!/bin/bash -l

################# GATK gVCF combining #################
# gVCFs produced in previous step should be now combined to allow for subsequent joined calling.

GATK=dir/to/gatk
DIR=dir/to/gvcfs/
REF=dir/to/REF_GENOME/guppy.fa
TMP=dir/to/temporary_files/tmp/

# Note that file names are just our examples.
${GATK} CombineGVCFs \
-R ${REF} \
--variant ${DIR}/T7-A.g.vcf.gz \
--variant ${DIR}/T7-F-1.g.vcf.gz \
--variant ${DIR}/T7-F-2.g.vcf.gz \
--variant ${DIR}/T7-F-3.g.vcf.gz \
--variant ${DIR}/T7-F-4.g.vcf.gz \
--variant ${DIR}/T7-J-1.g.vcf.gz \
--variant ${DIR}/T7-J-2.g.vcf.gz \
--variant ${DIR}/T7-J-3.g.vcf.gz \
--variant ${DIR}/T7-J-4.g.vcf.gz \
--variant ${DIR}/T7-M-1.g.vcf.gz \
--variant ${DIR}/T7-M-2.g.vcf.gz \
--variant ${DIR}/T7-O.g.vcf.gz \
-O T7_family_final.g.vcf.gz

${GATK} CombineGVCFs \
-R ${REF} \
--variant ${DIR}/T10-A.g.vcf.gz \
--variant ${DIR}/T10-F-1.g.vcf.gz \
--variant ${DIR}/T10-F-2.g.vcf.gz \
--variant ${DIR}/T10-J-1.g.vcf.gz \
--variant ${DIR}/T10-J-2.g.vcf.gz \
--variant ${DIR}/T10-J-3.g.vcf.gz \
--variant ${DIR}/T10-J-4.g.vcf.gz \
--variant ${DIR}/T10-J-5.g.vcf.gz \
--variant ${DIR}/T10-J-6.g.vcf.gz \
--variant ${DIR}/T10-M-1.g.vcf.gz \
--variant ${DIR}/T10-M-2.g.vcf.gz \
--variant ${DIR}/T10-O.g.vcf.gz \
-O T10_family_final.g.vcf.gz

# In this step two genomic VCF files for our two families separately are produced.
