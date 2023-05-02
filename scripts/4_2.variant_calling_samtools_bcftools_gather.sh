#!/bin/bash

################# VCFs merging #################
# By now, one has all chromome files for all individuals. These files can further merged to produce one file
# for whole genome for all individuals.

PIC=dir/to/picard.jar
DIR=dir/to/chromosome_vcfs

## Combine
java -Xmx60g -jar ${PIC} GatherVcfs \
TMP_DIR=dir/to/temporary_files \
R=dir/to/ref/guppy.fa \
O=${DIR}/ALL.vcf.gz \
I=${DIR}/vcf_list.txt # This is a list of vcf files from all scaffolds with combined individuals.

# The ALL file needs to be indexed.
tabix ${DIR}/ALL.vcf.gz
