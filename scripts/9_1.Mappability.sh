#!/bin/bash

################# Mappability of genomic sites #################
# Not all genomic sites can be mapped equally well, to find sites that may be ambigous, we ran GenMap
# on the reference genome.

# First, index the reference genome
genmap index -F reference.fasta -I /dir/to/index/folder

# Second, calculate the mappability scores across the genome
# -K stands for k-mer length; -E stands for number of mismatches
# -bg is particularly useful as it creates a BED file that can be later used with bedtools
genmap map -K 150 -E 3 -I /dir/to/index/folder -O /path/to/output/folder -t -w -bg
