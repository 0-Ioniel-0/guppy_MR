#!/bin/bash

################# BAM Surgeon faciliated FNR estimation #################
# To find how many variants may remain undetected (FNR) we created in-silico BAM file and then
# used it for calling with our two methods, then intersected resulting VCF files. Here's how
# the synthethic file was created.

ADDSNV=dir/to/BAMsurgeon/bin/addsnv.py
BED=variants_to_add.bed
BAM=ORIGINAL.bam
REF=reference_genome.fasta
PICARD=picard.jar

# Creating new in-silico BAM with BAMSurgeon
# -v bed file was created according to the tool manual and consisted of 5 columns: 
# chrom; pos_start; pos_end; new_allele_fraction; new_allele.
python ${ADDSNV} -v ${BED} --ignoresnps --ignoreref --force -p 10 \
 --aligner mem --picardjar ${PICARD} -f ${BAM} -r ${REF} -o preSILICO.bam

# Since newly inserted mutations tend to distrupt the reads; extracting them and remaping 
# has to be done. In order to retrieve reads from BAM file, name sorting order is needed.
samtools sort -n -@ 15 -o QpreSILICO.bam preSILICO.bam
# Reads extraction.
samtools fastq -@ 10 -N -1 N/new_1.fastq.gz -2 N/new_fastq.gz QpreSILICO.bam

bgzip -d silico_1.fastq.gz
bgzip -d silico_2.fastq.gz
# One needs to make sure that post-BAMSurgeon reads are properly paired.
fastq_pair silico_1.fastq silico_2.fastq

# Now, having FASTQ files, one can move to the mapping-related script (2_2) to create finalSILICO.bam file 
# and continue through all the calling steps until HF and ML DNM candidates are obtained for synthethic mutations.