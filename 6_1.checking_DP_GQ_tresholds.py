# STATS OF HETERO/HOMO
# This script retrieves DP and GQ info from specific types of two variants.
# 1) Mendelian variants, where offspring is a heterozygote (0/1) and parents are homozygotes (0/0 and 1/1)
# 2) non-Mendelian variants, where offspring is a homozygote (0/0 or 1/1) and parents are homozygotes (0/0 and 1/1)
# These variants DP and GQ are then plotted in R to obtain distributions from each parents-offspring trio in two cases
# described above.

import sys

file_in = sys.argv[1]  # input vcf file
mOther = int(sys.argv[2])  # mother position in the input file - 1
fAther = int(sys.argv[3])  # father position in the input file - 1
Kid = int(sys.argv[4])  # kid position in the input file - 1
fileHE_ODP = sys.argv[5]  # output file with mother DPs in offspring heterozygotes
fileHE_OGQ = sys.argv[6]  # output file with mother GQs in offspring heterozygotes
fileHE_ADP = sys.argv[7]  # output file with father DPs in offspring heterozygotes
fileHE_AGQ = sys.argv[8]  # output file with father GQs in offspring heterozygotes
fileHE_KDP = sys.argv[9]  # output file with kid DPs in offspring heterozygotes
fileHE_KGQ = sys.argv[10]  # output file with kid GQs in offspring heterozygotes
fileHO_ODP = sys.argv[11]  # output file with mother DPs in offspring homozygotes
fileHO_OGQ = sys.argv[12]  # output file with mother GQs in offspring homozygotes
fileHO_ADP = sys.argv[13]  # output file with father DPs in offspring homozygotes
fileHO_AGQ = sys.argv[14]  # output file with father GQs in offspring homozygotes
fileHO_KDP = sys.argv[15]  # output file with kid DPs in offspring homozygotes
fileHO_KGQ = sys.argv[16]  # output file with kid GQs in offspring homozygotes

# First, let's load a file.
print("Hello!")
print("Let's start!")
original_vcf: TextIO = open(file_in, 'r')
lines = original_vcf.readlines()

#
for v, variant in enumerate(lines, start=0):

    if variant.startswith('#'):
        continue  # Skip the header
    else:
        spl = variant.split("\t")

        # Info on father.
        father = spl[fAther].split(":")
        father_gt = father[0]
        father_dp = father[2]
        father_gq = father[3]

        # Info on offspring.
        kid = spl[Kid].split(":")
        kid_gt = kid[0]
        kid_dp = kid[2]
        kid_gq = kid[3]

        # Info on mother.
        mother = spl[mOther].split(":")
        mother_gt = mother[0]
        mother_dp = mother[2]
        mother_gq = mother[3]

        if ((mother_gt == ("0/0" or "0|0") and father_gt == ("1/1" or "1|1")) or
            (mother_gt == ("1/1" or "1|1") and father_gt == ("0/0" or "0|0"))) and \
                kid_gt == ("0/1" or "1/0" or "0|1" or "1|0"):
            with open(fileHE_ODP, 'a') as f:
                print(mother_dp, file=f, end="")
            with open(fileHE_ADP, 'a') as g:
                print(father_dp, file=f, end="")
            with open(fileHE_KDP, 'a') as h:
                print(kid_dp, file=f, end="")
            with open(fileHE_OGQ, 'a') as i:
                print(mother_gq, file=f, end="")
            with open(fileHE_AGQ, 'a') as j:
                print(father_gq, file=f, end="")
            with open(fileHE_KGQ, 'a') as k:
                print(kid_gq, file=f, end="")
        elif ((mother_gt == ("0/0" or "0|0") and father_gt == ("1/1" or "1|1")) or
              (mother_gt == ("1/1" or "1|1") and father_gt == ("0/0" or "0|0"))) and \
                kid_gt == ("0/0" or "1/1" or "0|0" or "1|1"):
            with open(fileHO_ODP, 'a') as f:
                print(motHOr_dp, file=f, end="")
            with open(fileHO_ADP, 'a') as g:
                print(fatHOr_dp, file=f, end="")
            with open(fileHO_KDP, 'a') as h:
                print(kid_dp, file=f, end="")
            with open(fileHO_OGQ, 'a') as i:
                print(motHOr_gq, file=f, end="")
            with open(fileHO_AGQ, 'a') as j:
                print(fatHOr_gq, file=f, end="")
            with open(fileHO_KGQ, 'a') as k:
                print(kid_gq, file=f, end="")
        else:
            continue

# LOOP ENDS HERE

original_vcf.close()
print("Printing DP/GQ done.")
