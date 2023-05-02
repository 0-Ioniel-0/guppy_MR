#!/bin/bash

################# TRIMMING and Quality Control #################
# Reads need to be trimmed to improve their quality. The most important thing is to get rid of Illumina adapters.
# Trimming also divides reads into paired and unpaired ones.
# Quality control must be performed before AND after trimming to see whether this step was successful.

# FastQC tool for quality control
FQC=dir/to/tools/fastQC/fastqc
# Trimmomatic tool
TRIMM=dir/to/tools/Trimmomatic/trimmomatic.jar
# Illumina adapters used
ADAPTERS=dir/to/tools/Trimmomatic/adapters/CD_indexes_adapters.fa
# Raw Illumina reads
IN=dir/to/RAW_DATA
# Trimmed reads
OUT=dir/to/TRIMMED
# Samples file
SAMPLE=$1

# Quality Control of raw reads
${FQC} --outdir=${IN}/QC ${IN}/${SAMPLE}_1.fastq.gz
${FQC} --outdir=${IN}/QC ${IN}/${SAMPLE}_2.fastq.gz
# Specify number of threads available (n), PE optiom idicates pair-end data
java -jar ${TRIMM} PE -phred33 ${IN}/${SAMPLE}_1.fastq.gz ${IN}/${SAMPLE}_2.fastq.gz \
-threads n -baseout ${OUT}/${X}.fastq.gz ILLUMINACLIP:$ADAPTERS:3:30:10 \
LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:40
# Quality Control of trimmed reads (only paired ones!)
${FQC} --outdir=${IN}/QC ${OUT}/${SAMPLE}_1P.fastq.gz
${FQC} --outdir=${IN}/QC ${OUT}/${SAMPLE}_2P.fastq.gz