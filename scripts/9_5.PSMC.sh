#!/bin/bash

################# PSMC - demography reconstruction #################
# Parental consensus genomes can be used to infere demographic history using PSMC

# We used -H I because we wanted to save info on heterozygotes.
bcftools consensus -H I -f reference_genome.fasta -o individual.fasta individual.vcf.gz

# Then PSMC was created using following commands.
# Since typical method for combining bootstrap to the main plot didn't work, we used workaround
# proposed by GitHub user "davidaray" (https://github.com/lh3/psmc/issues/26) which worked perfectly.
# Thank YOU, davidaray!
dir/to/psmc/utils/fq2psmcfa individual.fasta > individual.psmcfa
dir/to/psmc/utils/splitfa individual.psmcfa > individualsplit.psmca
dir/to/psmc/psmc -N25 -t15 -r5 -p "4+25*2+4+6" -o individual.psmc individual.psmcfa
seq 50 | xargs -i dir/to/psmc/psmc -N25 -t15 -r5 -b -p "4+25*2+4+6" \
-o individualround-{}.psmc individualsplit.psmca | sh
cat individual.psmc individualround-*.psmc > individual_combined.psmc
dir/to/psmc/utils/psmc_plot.pl -g 0.5 -u 2.9-e09 -R -p individual.plot.psmc individual_combined.psmc
# Then individual.plot.psmc file needs to be opened in Excel or R-studio to finally draw a plot using
# first (x) and second (y) column.
