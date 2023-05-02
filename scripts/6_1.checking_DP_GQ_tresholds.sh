#!/bin/bash

################# checking DP/GQ tresholds #################
# We checked DP and GQ in variants with Mendelian and non-Mendelian offspring genotypes.
# To get the values, python (3.5) script was used. It has 4 inputs and 12 outputs.
# Then R was used to plot values from the output files.

input_1=file.vcf
input_2=$1 # mother position in the input file - 1
input_3=$2 # father position in the input file - 1
input_4=$3 # kid position in the input file - 1
offspring_name=$4 # name of the offpring from the trio
output_1=${offspring_name}_mendelian_mother_DP.txt
output_1=${offspring_name}_mendelian_mother_GQ.txt
output_1=${offspring_name}_mendelian_father_DP.txt
output_1=${offspring_name}_mendelian_father_GQ.txt
output_1=${offspring_name}_mendelian_offspring_DP.txt
output_1=${offspring_name}_mendelian_offspring_GQ.txt
output_1=${offspring_name}_nonmendelian_mother_DP.txt
output_1=${offspring_name}_nonmendelian_mother_GQ.txt
output_1=${offspring_name}_nonmendelian_father_DP.txt
output_1=${offspring_name}_nonmendelian_father_GQ.txt
output_1=${offspring_name}_nonmendelian_offspring_DP.txt
output_1=${offspring_name}_nonmendelian_offspring_GQ.txt

python 6_1.checking_DP_GQ_tresholds.py \
${input_1} \
${input_2} \
${input_3} \
${input_4} \
${output_1} \
${output_2} \
${output_3} \
${output_4} \
${output_5} \
${output_6} \
${output_7} \
${output_8} \
${output_9} \
${output_10} \
${output_11} \
${output_12}
