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

Note that some scripts need to be edited to change DP thresholds and individuals' positions in the VCF files (also header length in some cases).
