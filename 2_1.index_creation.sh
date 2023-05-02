#!/bin/bash

################# Index Creation #################
# In order to map reads to the reference genome, 
# it must be indexed first with the same bwa, alignment is going to be performed with.

REF=/dir/to/reference/ref.fasta

# Guppy genome is ~700MB so it's big enough to index it with a 'bwtsw' method designed for big genomes.
bwa index -p Prefix -a bwtsw ${REF}

# Variant calling step also requires index, but this time it's different.
samtools faidx ${REF}