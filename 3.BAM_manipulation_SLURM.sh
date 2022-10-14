#!/bin/bash -l

##BASH -N 1
##BASH -n 
##BASH --time=10:00:00
##BASH --mem=60G

# Loading SLURM modules #
module load samtools/1.6.0

# Getting sample name. Provided by outside loop. All samples run in the same time. #
sample=$1

# Providing directories #
IN=dir/to/${sample}.bam
PIC=dir/to/tools/picard/picard.jar
TD=dir/to/temporary/files
library='NEB_Next_Ultra_II_FS'
platform='Illumina_Novaseq_6000'
unit='unit_1'

# Sorting reads by query name #
samtools sort -@ 5 -O bam -n -m 100M -o ${IN}.qsorted.bam ${IN}

# Fixing reads mates #
samtools fixmate -@ 5 -O bam ${IN}.mates_fixed.bam ${IN}.qsorted.bam

# Sorting reads by coordinate #
samtools sort -@ 5 -m 100M -O bam -o ${IN}.csorted.bam ${IN}.mates_fixed.bam
samtools index ${IN}.csorted.bam

# Marking and removing duplicates #
java -Xmx60G -jar ${PIC} MarkDuplicates \
        I=${IN}.csorted.bam \
        O=${IN}.rm_dup.bam \
        M=${input_bam}.txt \
        TMP_DIR=${TD} \
        CREATE_INDEX=true \
        REMOVE_DUPLICATES=true |\

# Adding Read Groups #
java -Xmx60G -jar ${PIC} AddOrReplaceReadGroups \
        I=${IN}.rm_dup.bamm \
        O=${DIR}/${sample}_ready.bam \
        RGLB=${library} \
        RGPL=${platform} \
        RGPU=${unit} \
        RGSM=${sample} \
        CREATE_INDEX=true

# Remove intermediate files #
rm ${IN}.qsorted.bam
rm ${IN}.mates_fixed.bam
rm ${IN}.csorted.bam
rm ${IN}.csorted.bam.bai
rm ${IN}.rm_dup.bam
rm ${IN}.rm_dup.bam.bai

# Calling-ready file is produced #
