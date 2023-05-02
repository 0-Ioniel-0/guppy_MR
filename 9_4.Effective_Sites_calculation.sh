#!/bin/bash

################# Effective Sites Calculation #################
# To screen for all sites that could have possibly contain a DNM, whole genomes of all trios needs to be filtered according to
# DP and GQ tresholds, mappability and repetitive regions masking. This is where gVCF files generated in script (4_3) are used 
# again. It might be useful to use chromosomal gVCFs (chromosome/file) to save time and resources.

mother_DPd=25
mother_DPu=102
father_DPd=28
father_DPu=112
offspring_DPd=23
offspring_DPu=90
GQ=70

# Filtering trio gVCFs by DP and GQ.
bcftools view -i "FORMAT/DP>=${mother_DPd} && FORMAT/DP<=${mother_DPu} && FORMAT/GQ>=${GQ}" -O v -o DPGQ_mother.g.vcf mother.g.vcf
bcftools view -i "FORMAT/DP>=${father_DPd} && FORMAT/DP<=${father_DPu} && FORMAT/GQ>=${GQ}" -O v -o DPGQ_father.g.vcf father.g.vcf
bcftools view -i "FORMAT/DP>=${offspring_DPd} && FORMAT/DP<=${offspring_DPu} && FORMAT/GQ>=${GQ}" -O v -o DPGQ_offspring.g.vcf offspring.g.vcf

# Creating BED files from filtered gVCF files. In awk $1 is chromosome, $2 is position_start and $2+s is position_end
grep -v '^#' DPGQ_mother.g.vcf | awk -v s=1 '{print $1 "	" $2 "	" $2+s}' > DPGQ_mother.bed
grep -v '^#' DPGQ_father.g.vcf | awk -v s=1 '{print $1 "	" $2 "	" $2+s}' > DPGQ_father.bed
grep -v '^#' DPGQ_offspring.g.vcf | awk -v s=1 '{print $1 "	" $2 "	" $2+s}' > DPGQ_offspring.bed

# Creating intervals form bp_resolution.
bedtools merge -i DPGQ_mother.bed > intervals_DPGQ_mother.bed
bedtools merge -i DPGQ_father.bed > intervals_DPGQ_father.bed
bedtools merge -i DPGQ_offspring.bed > intervals_DPGQ_offspring.bed

# Intersecting BED files.
# First, parents.
bedtools intersect -a intervals_DPGQ_mother.bed -b intervals_DPGQ_father.bed > intervals_DPGQ_parents.bed
# Second, parental BED with offspring BED.
bedtools intersect -a intervals_DPGQ_parents.bed -b intervals_DPGQ_offspring.bed > intervals_DPGQ_trio.bed

# Finally one needs to subtract sites that have mappability lower than 1 and sites in repetitve regions.
# Candidate DNMs should be screened similarly to how it's shown here (with bedtools subtract).
bedtools subtract -a intervals_DPGQ_trio.bed -b mappability.bed > mappability_intervals_DPGQ_trio.bed
bedtools subtract -a mappability_intervals_DPGQ_trio.bed -b repeats.bed > final_trio.bed

# To calculate final number of sites in given offspring one can use awk.
awk '{ sum += $3 - $2 } END { print sum }' final_trio.bed