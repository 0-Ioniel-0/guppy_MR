#!/bin/bash -l

#SBATCH -N 1
#SBATCH -n 20
#SBATCH --time=72:00:00
#SBATCH --mem=60gb

module load java8

# It's best to use newest version of GATK(4.3)
GA=dir/to/gatk
IN=dir/to/ready_bams/MAPPED
OU=dir/to/vcf/GATK
RE=dir/to/REF_GENOME/guppy.fna

# Sample name from the outside loop #
i=$1

${GA} --java-options "-Xmx60g" HaplotypeCaller \
-R ${RE} \
-I ${IN}/${i}_ready.bam \
-O ${OU}/${i}.g.vcf.gz \
-ERC BP_RESOLUTION \
--pcr-indel-model NONE \
--output-mode EMIT_ALL_CONFIDENT_SITES \
--native-pair-hmm-threads 20
