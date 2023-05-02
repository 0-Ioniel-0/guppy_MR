#!/bin/bash

################# GATK variant calling #################
# In GATK, a genomic VCF (gVCF) is firstly produced for each individual separately.

# It's best to use newest version of GATK
GA=dir/to/gatk
IN=dir/to/ready_bams/MAPPED
OU=dir/to/vcf/GATK
RE=dir/to/REF_GENOME/guppy.fna

# Sample name #
sample=$1

${GA} --java-options "-Xmx60g" HaplotypeCaller \
-R ${RE} \
-I ${IN}/${sample}.bam \
-O ${OU}/${sample}.g.vcf.gz \
-ERC BP_RESOLUTION \
--pcr-indel-model NONE \
--output-mode EMIT_ALL_CONFIDENT_SITES \
--native-pair-hmm-threads 20

# In the above command, BP_RESOLUTION and EMIT_ALL_CONFIDENT_SITES is important for following Effective Sites number calculation;
# --pcr-indel-model NONE should only be used if your genomic library was PCR-free;
# the last line is about available threads, 20 is just our example.
