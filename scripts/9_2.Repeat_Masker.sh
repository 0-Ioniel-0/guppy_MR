#!/bin/bash

################# Masking Repeats #################
# Note that we used Danio rerio repeats, because guppy specific repeats were not available.
RepeatMasker -pa 20  -gff -species danio genome.fna
