# guppy_MR
Repository for all scripts used to estimate guppy (Poecilia reticulata) mutation rate.

This repository contains scripts regarding:
1) reads trimming
2) reads alignment
3) bam files manipulation
4) variant calling
5) vcf intersection and missing parents removal
6) finding de novo variants
7) finding callable genomic sites
8) preparing variants for DNMF filter
9) hard filtering of candidates
10) heterozygosity in family
11) BAMSurgeon simulation (FNR)

The scripts were run on the Poznan Supercomputing and Networking Center cluster, using SLURM job scheduler. Some programs were preinsatlled on the cluster and load as modules.

Note that most of the scripts need to be edited to change paths to files and programs. DP thresholds, individuals' positions in the VCF files, header length etc. should also be modified accordingly.

For help or comments, contact: k.burda[a]amu.edu.pl


