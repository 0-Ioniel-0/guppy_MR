# Guppy Mutation Rate Estimation
Repository for all scripts used to estimate guppy (*Poecilia reticulata*) mutation rate.

## This repository contains scripts regarding:
1) reads trimming
2) reads alignment
3) bam files manipulation
4) variant calling
6) finding de novo variants
7) finding callable genomic sites
8) preparing variants for DNMFilter tools (ML filtering)
9) hard filtering of candidates
10) basic statistics in family VCF file
11) BAMSurgeon simulation (False Negative Rate estimation)
and more..

!!! For details on the workflow of this project, please look into ***flowchart.png*** figure. !!!

<sub>Note that most of the scripts need to be edited to change paths to files and programs. DP thresholds, number of individuals, individuals' positions in the VCF files etc. should also be modified accordingly. A sample VCF file is provided. <sub>

### These scripts were run with:
  - Python (3.5)
  - FastQC (0.11.8)
  - Trimmomatic (0.39)
  - bwa (0.7.10)
  - samtools (1.6.0)
  - bcftools (1.9)
  - gatk (4.1.4.1)
  - vcftools (0.1.14)
  - DNMFilter (0.1.1)
  - bedtools (2.27.1)
  - BAMSurgeon (1.4.1)
  - PSMC (0.6.5)
  - GenMap (1.3.0)
  - RepeatMasker ()

<sub>For help or comments, contact: k.burda[a]amu.edu.pl<sub>
