#!/bin/bash -l

#SBATCH --time=24:00:00
#SBATCH -n 28

module load java8


################# TRIMMING ################# 

# Trimmomatic tool
TRIMM=dir/to/tools/Trimmomatic-0.39/trimmomatic-0.39.jar
# Illumina adapters used
ADAPTERS=dir/to/tools/Trimmomatic-0.39/adapters/CD_indexes_adapters.fa
# Raw Illumina reads
IN=dir/to/RAW_DATA
# Trimmed reads
OUT=dir/to/TRIMMED
# List o samples
LIST=dir/to/list.txt

while read X

        do

java -jar $TRIMM PE -phred33 ${IN}/${X}_1.fastq.gz ${IN}/${X}_2.fastq.gz \
-threads 28 -baseout ${OUT}/${X}.fastq.gz ILLUMINACLIP:$ADAPTERS:3:30:10 \
LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:40

        done < ${LIST}
