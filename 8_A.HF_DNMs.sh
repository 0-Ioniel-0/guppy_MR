#!/bin/bash

################# Hard Filtering of de novo DNMs #################
# Set of candidate mutations was hard filtered adding three additional filters: 1) INFO-field statistics
# 2) AB in offspring 3) AD in parents. The DP and GQ values need to be added yet again.
# This script produces two files: VCF file with whole variants, TXT file which points to mutations. 
# Note that all values and names here are just our examples. 

input=de_novo_T7.vcf
output1=Hard_Filtering_DNMs.vcf
output2=Hard_Filtering_DNMs.txt

AD=0
ABd=0.3
ABu=0.7
FS=60
MQ=40
MQRankSum=-12.5
ReadPosRankSum=-8
SOR=3
QUAL_DP=2
GQ=70 # GQ treshold, here's our example
aDd=28 # lower DP treshold for father
aDu=112 # upper DP treshold for father
oDd=25 # lower DP treshold for mother
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
python 8_A.DNM_hard_filtering.py ${input} ${output1}  ${output2} \
${oDd} ${aDd} ${k1Dd} ${k2Dd} ${k3Dd} ${k4Dd} ${k5Dd} ${k6Dd} ${k7Dd} ${k8Dd} ${k9Dd} ${k10Dd} \
${oDu} ${aDu} ${k1Du} ${k2Du} ${k3Du} ${k4Du} ${k5Du} ${k6Du} ${k7Du} ${k8Du} ${k9Du} ${k10Du} \
${AD} ${ABd} ${ABu} ${FS} ${MQ} ${MQRankSum} ${ReadPosRankSum} ${SOR} ${QUAL_DP} ${GQ}