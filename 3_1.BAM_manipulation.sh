#!/bin/bash

################# BAM Manipulation #################
# BAM file produced in the previous step is still imperfect. It's best to remove not needed duplicates,
# which in result, makes files smaller. It's obligatory to add RG (read group) so that each sample has unique
# description and known sequencing run. For example, we resequenced T10 mother two times and each resequencing
# had different platform which was noted in RG.

# Sample name.
sample=$1

# Providing directories #
IN=dir/to/${sample}.bam
PIC=dir/to/tools/picard/picard.jar
TD=dir/to/temporary/files
library='NEB_Next_Ultra_II_FS' # that's our example
platform='Illumina_Novaseq_6000' # that's our example
unit='unit_1' # that's our example

# Sorting reads by query name #
# First BAM need to be sorted by reads names for next step.
# No index can be created for query-sorted BAM files.
samtools sort -@ 5 -O bam -n -m 100M -o ${IN}.qsorted.bam ${IN}

# Fixing reads mates #
samtools fixmate -@ 5 -O bam ${IN}.mates_fixed.bam ${IN}.qsorted.bam

# Sorting reads by coordinate #
# Following step requires reads to by sorted by position in reference genome.
# Also index is obligatory.
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

# Calling-ready file has been created by now #