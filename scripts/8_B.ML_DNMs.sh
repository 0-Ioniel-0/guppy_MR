#!/bin/bash

################# ML Filtering of de novo DNMs #################
# Giving that one already has training set moleculary validated, the process may begin.
# Firstly tool gathers data. Then it filters.

DNM_filter=DNMFilter.jar
REF=genome.fa  # Reference genome
PED=family.ped  # Family pedigree file prepared as described in the tool manual
POS=pos.csv  # CSV file of molecularly validated TRUE positives
NEG=neg.csv  # CSV file of molecularly validated FALSE positives
BAM=bam.list  # List of BAM files of family members mentioned in PED file
TRA=training_set.csv # OUTPUT - Training set characteristics file

java -Xmx40g -jar ${DNM_filter} extract \
--reference ${REF} \
--pedigree      ${PED} \
--positive      ${POS} \
--negative      ${NEG} \
--bam           ${BAM} \
--output        ${TRA}

DNM_filter=DNMFilter.jar
REF=genome.fa  # Reference genome
PED=family.ped  # Family pedigree file prepared as described in the tool manual
BAM=bam.list  # List of BAM files of family members mentioned in PED file
TRA=training_set.csv  # Training set characteristics file prepared in previous step
CAN=can.csv  # Candidates CSV file
CON=Features.conf  # File containing list of fearures to take into consideration (1 = applied, 0 = not applied)
OUT=ML_filtered_DNMs.csv  # Output file

java -Xmx40g -jar ${DNM_filter} gbm \
--reference ${REF} \
--pedigree      ${PED} \
--bam           ${BAM} \
--training      ${TRA} \
--candidate     ${CAN} \
--configuration ${CON} \
--output                ${OUT}
