#!/bin/bash

################# finding de novo variants #################
# In this step, we looked for variants that are absent in parents and present in offspring (de novo)
# The only filters were DP and GQ. Note that all values and names here are just our examples. 

# Provide file of the family:
family='T7'
input=family_${family}.vcf
output=de_novo_${family}.vcf
output2=de_novo_${family}.csv
GQ=70 # GQ treshold, here's our example
aDd=28 # lower DP treshold for father
aDu=25 # upper DP treshold for father
oDd=102 # lower DP treshold for mother
oDu=112 # upper DP treshold for mother
k1Dd=23 # lower DP treshold for offspring...
k1Du=90 # upper DP treshold for offspring...
k2Dd=16
k2Du=62
k3Dd=19
k3Du=74
k4Dd=15
k4Du=56
k5Dd=20
k5Du=82
k6Dd=15
k6Du=40
k7Dd=17
k7Du=70
k8Dd=21
k8Du=84
k9Dd=18
k9Du=72
k10Dd=23
k10Du=94

# This script is written with 10 offspring in mind. If one has less or more offspring, they need to change the script accordingly
python 6_3.finding_de_novo_variants.py ${input} ${output} ${family} \
${oDd} ${aDd} ${k1Dd} ${k2Dd} ${k3Dd} ${k4Dd} ${k5Dd} ${k6Dd} ${k7Dd} ${k8Dd} ${k9Dd} ${k10Dd} \
${oDu} ${aDu} ${k1Du} ${k2Du} ${k3Du} ${k4Du} ${k5Du} ${k6Du} ${k7Du} ${k8Du} ${k9Du} ${k10Du} \
${GQ} ${output2}

# VCF file with DNM variants has been created. CSV file with exact DNMs has been created. It will later used in ML filtering.
