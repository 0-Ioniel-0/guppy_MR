<p style="font-size:20px;">guppy_MutationRateEstimation</p>
Repository for all scripts used to estimate guppy (Poecilia reticulata) mutation rate.

This repository contains scripts regarding:
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

For details on the workflow of this project, please look into flow_chart.pdf figure.

The scripts were run on the Poznan Supercomputing and Networking Center cluster, using SLURM job scheduler. Some programs were preinsatlled on the cluster and load as modules.

Note that most of the scripts need to be edited to change paths to files and programs. DP thresholds, number of individuals, individuals' positions in the VCF files etc. should also be modified accordingly.

To run these scripts you will need:


For help or comments, contact: k.burda[a]amu.edu.pl
