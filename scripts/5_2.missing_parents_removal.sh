#!/bin/bash

################# missing parents variants removal #################
# Variants with no information on parental genotype are useless so they can be removed.
# In our case, missing parents variants were removed using python script (to simultaneusly calculate removed sites), 
# but the same result can be obtained with bcftools view -e "GT[parental]="miss" option.

input=$1

# Unzipping is needed first.
bgzip -d ${input}.gz
# One must provide the script with parental field numbers (i.e. where mother and father are located in a vcf file),
# in our case that was 10th and 21st column, note that first column in Python is 0! The result of this script will
# also be a number of removed sites. Also, the script was used with Python 3.5
python missing_parents_removal.py ${input} no_missing_parents_${input} 9 20
# Finally file needs to be bgzipped again.
bgzip no_missing_parents_${input}

# In this step, VCF without missing parents is produced.
