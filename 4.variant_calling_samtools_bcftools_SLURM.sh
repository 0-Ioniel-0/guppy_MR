#!/bin/bash

#SBATCH --array=1-2767
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --mem=60gb
#SBATCH -p standard
#SBATCH --time=72:00:00

# SLURM modules #
module load samtools/1.6.0
module load bcftools/1.9
module load htslib
module load tabix

# Info on task ID (chromsome) and begining time #
echo Starting at 
date
echo $SLURM_ARRAY_TASK_ID

# All bams (individuals) must be listed in following list #
BAMLIST=dir/to/bams/list.txt
GENOME=dir/to/REF_GENOME/guppy.fa
# List of genomic scaffolds. Since calling whole genome needs too much time and resources, it's better to split it.  #
splitfile=dir/to/scaffolds.txt
OUT=dir/to/output/
chrsplit=$(awk 'NR=='$SLURM_ARRAY_TASK_ID'{print $1}' $splitfile)

# Samtools gathers all individuals and extract just one region at time. Remember to add -t DP,ADF,ADR #
samtools mpileup -R -t DP,ADF,ADR -vuf $GENOME -b $BAMLIST -r "${chrsplit}" -o ${OUT}/gvcf/tmp.${SLURM_ARRAY_TASK_ID}.raw.vcf
bgzip ${OUT}/gvcf/tmp.${SLURM_ARRAY_TASK_ID}.Guppy.var.raw.vcf && tabix ${OUT}/gvcf/tmp.${SLURM_ARRAY_TASK_ID}.raw.vcf.gz

# Bcftools calls variants. Remember to add -f GQ #
bcftools call -f GQ -vmO v -o ${OUT}/vcf/tmp.${SLURM_ARRAY_TASK_ID}.Guppy.SNPs.vcf ${OUT}/gvcf/tmp.${SLURM_ARRAY_TASK_ID}.Guppy.var.raw.vcf.gz
bgzip ${OUT}/vcf/tmp.${SLURM_ARRAY_TASK_ID}.Guppy.SNPs.vcf && tabix ${OUT}/vcf/tmp.${SLURM_ARRAY_TASK_ID}.Guppy.SNPs.vcf.gz

# Info on finishing time #
echo Finished at 
date
