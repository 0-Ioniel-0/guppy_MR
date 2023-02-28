#!/bin/bash

ADDSNV=/Bamsurgeon/adamewing-bamsurgeon-3f30d30/bin/addsnv.py
BED=variants.bed
BAM=Original.bam
REF=genome.fasta
PICARD=picard.jar

#Surgery
python3 $ADDSNV -v $BED --ignoresnps --ignoreref --force -p 10 \
 --aligner mem --picardjar $PICARD -f $BAM -r $REF -o SILICO.bam \
2>BAMsurgeon_log.txt

#Remap
samtools sort -n -@ 15 -o QSILICO.bam SILICO.bam
samtools fastq -@ 10 -N -1 N/new_1.fastq.gz -2 N/new_fastq.gz QSILICO.bam

bgzip -d N/new_1.fastq.gz
bgzip -d N/new_2.fastq.gz
#Make sure there are proper pairs
fastq_pair N/new_1.fastq N/new_2.fastq

#Now, having FASTQ files move to the mapping-related script
