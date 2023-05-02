# FINDING DE NOVO MUTATIONS
# One needs to provide input file, output file, family name, all individuals dp tresholds (parents first, offspring in the same order as in vcf file) and gq minimal value and header length (grep '^#' file | wc -l) 

from typing import List, TextIO
import sys

file_in = sys.argv[1]
file_out = sys.argv[2]
family = sys.argv[3]
file_out2 = sys.argv[29]

print("Hello!")
print("We are running DE NOVO MUTATIONS SCRIPT")
print("Family: ", family)
print("Working...")

# First, let's load vcf file.
original_vcf: TextIO = open(file_in, 'r')
lines = original_vcf.readlines()

# Next, quality tresholds.
# First the minimal value.
oDPd = int(sys.argv[4])
aDPd = int(sys.argv[5])
k1DPd = int(sys.argv[6])
k2DPd = int(sys.argv[7])
k3DPd = int(sys.argv[8])
k4DPd = int(sys.argv[9])
k5DPd = int(sys.argv[10])
k6DPd = int(sys.argv[11])
k7DPd = int(sys.argv[12])
k8DPd = int(sys.argv[13])
k9DPd = int(sys.argv[14])
k10DPd = int(sys.argv[15])
# Then, the max value.
oDPu = int(sys.argv[16])
aDPu = int(sys.argv[17])
k1DPu = int(sys.argv[18])
k2DPu = int(sys.argv[19])
k3DPu = int(sys.argv[20])
k4DPu = int(sys.argv[21])
k5DPu = int(sys.argv[22])
k6DPu = int(sys.argv[23])
k7DPu = int(sys.argv[24])
k8DPu = int(sys.argv[25])
k9DPu = int(sys.argv[26])
k10DPu = int(sys.argv[27])
# GQ.
GQ = int(sys.argv[28])

# Loop starts here.
for v, variant in enumerate(lines, start=0):

    # Printing header first.
    if variant.startswith('#'):
        with open(file_out, 'a') as f:
            print(variant, file=f, end="")

    # Now, main thing.
    else:

        # Splitting variant into fields.
        spl: List[str] = variant.split("\t")

        # Getting info on father, GT/DP/GQ.
        father_s = spl[9].split(":")
        father = father_s[0]
        father_DP_check = father_s[2]
        if father_DP_check is ".":
            father_DP = 0
        else:
            father_DP = int(father_DP_check)
        father_GQ_check = father_s[3]
        if father_GQ_check is ".":
            father_GQ = 0
        else:
            father_GQ = int(father_GQ_check)

        # Getting info on kid nr 1, GT/DP/GQ.
        kid_1_s = spl[10].split(":")
        kid_1 = kid_1_s[0]
        # Autosomes and Scaffold.
        if len(kid_1) > 1:
            kid_1_1 = list(kid_1)[0]
            kid_1_2 = list(kid_1)[2]
        # Mitochondrium.
        else:
            kid_1_1 = kid_1
            kid_1_2 = kid_1
        kid_1_DP_check = kid_1_s[2]
        if kid_1_DP_check is ".":
            kid_1_DP = 0
        else:
            kid_1_DP = int(kid_1_DP_check)
        kid_1_GQ_check = kid_1_s[3]
        if kid_1_GQ_check is ".":
            kid_1_GQ = 0
        else:
            kid_1_GQ = int(kid_1_GQ_check)

        # Getting info on kid nr 2, GT/DP/GQ.
        kid_2_s = spl[11].split(":")
        kid_2 = kid_2_s[0]
        if len(kid_2) > 1:
            kid_2_1 = list(kid_2)[0]
            kid_2_2 = list(kid_2)[2]
        else:
            kid_2_1 = kid_2
            kid_2_2 = kid_2
        kid_2_DP_check = kid_2_s[2]
        if kid_2_DP_check is ".":
            kid_2_DP = 0
        else:
            kid_2_DP = int(kid_2_DP_check)
        kid_2_GQ_check = kid_2_s[3]
        if kid_2_GQ_check is ".":
            kid_2_GQ = 0
        else:
            kid_2_GQ = int(kid_2_GQ_check)

        # Getting info on kid nr 3, GT/DP/GQ.
        kid_3_s = spl[12].split(":")
        kid_3 = kid_3_s[0]
        if len(kid_3) > 1:
            kid_3_1 = list(kid_3)[0]
            kid_3_2 = list(kid_3)[2]
        else:
            kid_3_1 = kid_3
            kid_3_2 = kid_3
        kid_3_DP_check = kid_3_s[2]
        if kid_3_DP_check is ".":
            kid_3_DP = 0
        else:
            kid_3_DP = int(kid_3_DP_check)
        kid_3_GQ_check = kid_3_s[3]
        if kid_3_GQ_check is ".":
            kid_3_GQ = 0
        else:
            kid_3_GQ = int(kid_3_GQ_check)

        # Getting info on kid nr 4, GT/DP/GQ.
        kid_4_s = spl[13].split(":")
        kid_4 = kid_4_s[0]
        if len(kid_4) > 1:
            kid_4_1 = list(kid_4)[0]
            kid_4_2 = list(kid_4)[2]
        else:
            kid_4_1 = kid_4
            kid_4_2 = kid_4
        kid_4_DP_check = kid_4_s[2]
        if kid_4_DP_check is ".":
            kid_4_DP = 0
        else:
            kid_4_DP = int(kid_4_DP_check)
        kid_4_GQ_check = kid_4_s[3]
        if kid_4_GQ_check is ".":
            kid_4_GQ = 0
        else:
            kid_4_GQ = int(kid_4_GQ_check)

        # Getting info on kid nr 5, GT/DP/GQ.
        kid_5_s = spl[14].split(":")
        kid_5 = kid_5_s[0]
        if len(kid_5) > 1:
            kid_5_1 = list(kid_5)[0]
            kid_5_2 = list(kid_5)[2]
        else:
            kid_5_1 = kid_5
            kid_5_2 = kid_5
        kid_5_DP_check = kid_5_s[2]
        if kid_5_DP_check is ".":
            kid_5_DP = 0
        else:
            kid_5_DP = int(kid_5_DP_check)
        kid_5_GQ_check = kid_5_s[3]
        if kid_5_GQ_check is ".":
            kid_5_GQ = 0
        else:
            kid_5_GQ = int(kid_5_GQ_check)

        # Getting info on kid nr 6, GT/DP/GQ.
        kid_6_s = spl[15].split(":")
        kid_6 = kid_6_s[0]
        if len(kid_6) > 1:
            kid_6_1 = list(kid_6)[0]
            kid_6_2 = list(kid_6)[2]
        else:
            kid_6_1 = kid_6
            kid_6_2 = kid_6
        kid_6_DP_check = kid_6_s[2]
        if kid_6_DP_check is ".":
            kid_6_DP = 0
        else:
            kid_6_DP = int(kid_6_DP_check)
        kid_6_GQ_check = kid_6_s[3]
        if kid_6_GQ_check is ".":
            kid_6_GQ = 0
        else:
            kid_6_GQ = int(kid_6_GQ_check)

        # Getting info on kid nr 7, GT/DP/GQ.
        kid_7_s = spl[16].split(":")
        kid_7 = kid_7_s[0]
        if len(kid_7) > 1:
            kid_7_1 = list(kid_7)[0]
            kid_7_2 = list(kid_7)[2]
        else:
            kid_7_1 = kid_7
            kid_7_2 = kid_7
        kid_7_DP_check = kid_7_s[2]
        if kid_7_DP_check is ".":
            kid_7_DP = 0
        else:
            kid_7_DP = int(kid_7_DP_check)
        kid_7_GQ_check = kid_7_s[3]
        if kid_7_GQ_check is ".":
            kid_7_GQ = 0
        else:
            kid_7_GQ = int(kid_7_GQ_check)

        # Getting info on kid nr 8, GT/DP/GQ.
        kid_8_s = spl[17].split(":")
        kid_8 = kid_8_s[0]
        if len(kid_8) > 1:
            kid_8_1 = list(kid_8)[0]
            kid_8_2 = list(kid_8)[2]
        else:
            kid_8_1 = kid_8
            kid_8_2 = kid_8
        kid_8_DP_check = kid_8_s[2]
        if kid_8_DP_check is ".":
            kid_8_DP = 0
        else:
            kid_8_DP = int(kid_8_DP_check)
        kid_8_GQ_check = kid_8_s[3]
        if kid_8_GQ_check is ".":
            kid_8_GQ = 0
        else:
            kid_8_GQ = int(kid_8_GQ_check)

        # Getting info on kid nr 9, GT/DP/GQ.
        kid_9_s = spl[18].split(":")
        kid_9 = kid_9_s[0]
        if len(kid_9) > 1:
            kid_9_1 = list(kid_9)[0]
            kid_9_2 = list(kid_9)[2]
        else:
            kid_9_1 = kid_9
            kid_9_2 = kid_9
        kid_9_DP_check = kid_9_s[2]
        if kid_9_DP_check is ".":
            kid_9_DP = 0
        else:
            kid_9_DP = int(kid_9_DP_check)
        kid_9_GQ_check = kid_9_s[3]
        if kid_9_GQ_check is ".":
            kid_9_GQ = 0
        else:
            kid_9_GQ = int(kid_9_GQ_check)

        # Getting info on kid nr 10, GT/DP/GQ.
        kid_10_s = spl[19].split(":")
        kid_10 = kid_10_s[0]
        if len(kid_10) > 1:
            kid_10_1 = list(kid_10)[0]
            kid_10_2 = list(kid_10)[2]
        else:
            kid_10_1 = kid_10
            kid_10_2 = kid_10
        kid_10_DP_check = kid_10_s[2]
        if kid_10_DP_check is ".":
            kid_10_DP = 0
        else:
            kid_10_DP = int(kid_10_DP_check)
        kid_10_GQ_check = kid_10_s[3]
        if kid_10_GQ_check is ".":
            kid_10_GQ = 0
        else:
            kid_10_GQ = int(kid_10_GQ_check)

        # Getting info on mother, GT/DP/GQ.
        mother_s = spl[20].split(":")
        mother = mother_s[0]
        mother_DP_check = mother_s[2]
        if mother_DP_check is ".":
            mother_DP = 0
        else:
            mother_DP = int(mother_DP_check)
        mother_GQ_check = mother_s[3]
        if mother_GQ_check is ".":
            mother_GQ = 0
        else:
            mother_GQ = int(mother_GQ_check)

        # Setting variables for kids.
        kid_1_check = False
        kid_2_check = False
        kid_3_check = False
        kid_4_check = False
        kid_5_check = False
        kid_6_check = False
        kid_7_check = False
        kid_8_check = False
        kid_9_check = False
        kid_10_check = False

        # Part below checks whether either of two alleles in kids can be found in parents and whether parents and
        # kids DP and GQ are high enough (according to treshold set in the beginning of the file). If all these
        # conditions are met, the check variable is changed into True for particular kid.

        if (((kid_1_1 not in father) and (kid_1_1 not in mother) and kid_1_1 is not ".") or
            ((kid_1_2 not in father) and (kid_1_2 not in mother) and kid_1_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k1DPd <= kid_1_DP <= k1DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_1_GQ >= GQ:
            kid_1_check = True
        if (((kid_2_1 not in father) and (kid_2_1 not in mother) and kid_2_1 is not ".") or
            ((kid_2_2 not in father) and (kid_2_2 not in mother) and kid_2_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k2DPd <= kid_2_DP <= k2DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_2_GQ >= GQ:
            kid_2_check = True
        if (((kid_3_1 not in father) and (kid_3_1 not in mother) and kid_3_1 is not ".") or
            ((kid_3_2 not in father) and (kid_3_2 not in mother) and kid_3_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k3DPd <= kid_3_DP <= k3DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_3_GQ >= GQ:
            kid_3_check = True
        if (((kid_4_1 not in father) and (kid_4_1 not in mother) and kid_4_1 is not ".") or
            ((kid_4_2 not in father) and (kid_4_2 not in mother) and kid_4_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k4DPd <= kid_4_DP <= k4DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_4_GQ >= GQ:
            kid_4_check = True
        if (((kid_5_1 not in father) and (kid_5_1 not in mother) and kid_5_1 is not ".") or
            ((kid_5_2 not in father) and (kid_5_2 not in mother) and kid_5_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k5DPd <= kid_5_DP <= k5DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_5_GQ >= GQ:
            kid_5_check = True
        if (((kid_6_1 not in father) and (kid_6_1 not in mother) and kid_6_1 is not ".") or
            ((kid_6_2 not in father) and (kid_6_2 not in mother) and kid_6_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k6DPd <= kid_6_DP <= k6DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_6_GQ >= GQ:
            kid_6_check = True
        if (((kid_7_1 not in father) and (kid_7_1 not in mother) and kid_7_1 is not ".") or
            ((kid_7_2 not in father) and (kid_7_2 not in mother) and kid_7_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k7DPd <= kid_7_DP <= k7DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_7_GQ >= GQ:
            kid_7_check = True
        if (((kid_8_1 not in father) and (kid_8_1 not in mother) and kid_8_1 is not ".") or
            ((kid_8_2 not in father) and (kid_8_2 not in mother) and kid_8_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k8DPd <= kid_8_DP <= k8DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_8_GQ >= GQ:
            kid_8_check = True
        if (((kid_9_1 not in father) and (kid_9_1 not in mother) and kid_9_1 is not ".") or
            ((kid_9_2 not in father) and (kid_9_2 not in mother) and kid_9_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k9DPd <= kid_9_DP <= k9DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_9_GQ >= GQ:
            kid_9_check = True
        if (((kid_10_1 not in father) and (kid_10_1 not in mother) and kid_10_1 is not ".") or
            ((kid_10_2 not in father) and (kid_10_2 not in mother) and kid_10_2 is not ".")) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                k10DPd <= kid_10_DP <= k10DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_10_GQ >= GQ:
            kid_10_check = True

        # All kids check values are collected in a list.
        kids_check = [kid_1_check, kid_2_check, kid_3_check, kid_4_check, kid_5_check,
                      kid_6_check, kid_7_check, kid_8_check, kid_9_check, kid_10_check]

        # If any kid is marked True (as explained above), the variant is printed into the output VCF file.
        if any(kids_check):
            with open(file_out, 'a') as f:
                print(variant, file=f, end=" ")

        # Printing exact mutations into TXT file which will later be used by ML tool.
        if kid_1_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_1", file=f, end="")
        if kid_2_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_2", file=f, end="")
        if kid_3_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_3", file=f, end="")
        if kid_4_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_4", file=f, end="")
        if kid_5_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_5", file=f, end="")
        if kid_6_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_6", file=f, end="")
        if kid_7_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_7", file=f, end="")
        if kid_8_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_8", file=f, end="")
        if kid_9_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_9", file=f, end="")
        if kid_10_check is True:
            with open(file_out2, 'a') as f:
                print(spl[0], file=f, end=",")
                print(spl[1], file=f, end=",")
                print("kid_10", file=f, end="")

# Input file is closed here and the script ends.
original_vcf.close()

print("De-novo mutations found.")
