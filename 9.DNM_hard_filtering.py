# FINDING DE NOVO MUTATIONS

import sys

file_in = sys.argv[1]
file_out = sys.argv[2]
trash = sys.argv[3]

# First, let's load vcf file.

print("Hello!")
print("We are running DE NOVO MUTATIONS SCRIPT")
print("Working...")

original_vcf = open(file_in, 'r')

lines = original_vcf.readlines()

# Next, quality tresholds.
oDPd = 25
aDPd = 28
f1DPd = 23
f2DPd = 16
f3DPd = 19
f4DPd = 15
j1DPd = 20
j2DPd = 15
j3DPd = 17
j4DPd = 21
m1DPd = 18
m2DPd = 23
oDPu = 102
aDPu = 112
f1DPu = 90
f2DPu = 62
f3DPu = 74
f4DPu = 56
j1DPu = 82
j2DPu = 40
j3DPu = 70
j4DPu = 84
m1DPu = 72
m2DPu = 94

GQ = 70

QUAL_DP = 0
MQ = 0
FS = 100
SOR = 0
MQRankSum = -20
ReadPosRankSum = -20

# Loop starts here.
for v, variant in enumerate(lines, start=0):

    # Header first.
    if v < 2812:
        with open(file_out, 'a') as f:
            print(variant, file=f, end="")

    # Now, main thing.
    else:

        # Splitting variant into fields.
        spl = variant.split("\t")
        INFO = spl[7].split(";")
        INFO_VALUES = []

        # Getting variant QUAL and INFO filters
        for info in INFO:
            name = str(info.split("=")[0])
            print(name)
            value = info.split("=")[1]
            if name == "QD":
                value = float(value)
                QUAL_DP = value
                INFO_VALUES = INFO_VALUES + [name]
            elif name == "MQ":
                value = float(value)
                MQ = value
                INFO_VALUES = INFO_VALUES + [name]
            elif name == "FS":
                value = float(value)
                FS = value
                INFO_VALUES = INFO_VALUES + [name]
            elif name == "MQRankSum":
                value = float(value)
                MQRankSum = value
                INFO_VALUES = INFO_VALUES + [name]
            elif name == "ReadPosRankSum":
                value = float(value)
                ReadPosRankSum = value
                INFO_VALUES = INFO_VALUES + [name]
            elif name == "SOR":
                value = float(value)
                SOR = value
                INFO_VALUES = INFO_VALUES + [name]
            else:
                continue

        INFO_check = False

        print(len(INFO_VALUES))

        if len(INFO_VALUES) is 6:
            INFO_check = True

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

        # Getting info on parents AD.
        father_AD_check = father_s[1]
        mother_AD_check = mother_s[1]

        father_check = True
        if len(father_AD_check.split(",")) > 2:
            father_check = False
        mother_check = True
        if len(mother_AD_check.split(",")) > 2:
            mother_check = False

        father_AD_1 = int(father_AD_check.split(",")[0])
        father_AD_2 = int(father_AD_check.split(",")[1])

        mother_AD_1 = int(mother_AD_check.split(",")[0])
        mother_AD_2 = int(mother_AD_check.split(",")[1])

        if father_AD_1 > 0 and father_AD_2 > 0:
            father_check = False
        if mother_AD_1 > 0 and mother_AD_2 > 0:
            mother_check = False

        parents_check = False
        parents_AD = [father_check, mother_check]
        if all(parents_AD):
            parents_check = True

        # Getting info on kid nr 1, GT/DP/GQ.
        kid_1_s = spl[10].split(":")
        kid_1 = kid_1_s[0]
        kid_1_ad = kid_1_s[1]
        # Autosomes and Scaffold.
        if len(kid_1) > 1:
            kid_1_1 = list(kid_1)[0]
            kid_1_ad_1 = float(kid_1_ad.split(",")[0])
            kid_1_2 = list(kid_1)[2]
            kid_1_ad_2 = float(kid_1_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_1_1 = kid_1
            kid_1_2 = kid_1
            kid_1_ad_1 = 0
            kid_1_ad_2 = 0
        kid_1_DP_check = kid_1_s[2]
        if kid_1_DP_check is ".":
            kid_1_DP = 0
            kid_1_ab_1 = 0
            kid_1_ab_2 = 0
        else:
            kid_1_DP = int(kid_1_DP_check)
            if kid_1_DP == 0:
                kid_1_ab_1 = 0
                kid_1_ab_2 = 0
            else:
                kid_1_ab_1 = kid_1_ad_1 / float(kid_1_DP)
                kid_1_ab_2 = kid_1_ad_2 / float(kid_1_DP)
        kid_1_GQ_check = kid_1_s[3]
        if kid_1_GQ_check is ".":
            kid_1_GQ = 0
        else:
            kid_1_GQ = int(kid_1_GQ_check)

        # Getting info on kid nr 2, GT/DP/GQ.
        kid_2_s = spl[10].split(":")
        kid_2 = kid_2_s[0]
        kid_2_ad = kid_2_s[1]
        # Autosomes and Scaffold.
        if len(kid_2) > 1:
            kid_2_1 = list(kid_2)[0]
            kid_2_ad_1 = float(kid_2_ad.split(",")[0])
            kid_2_2 = list(kid_2)[2]
            kid_2_ad_2 = float(kid_2_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_2_1 = kid_2
            kid_2_2 = kid_2
            kid_2_ad_1 = 0
            kid_2_ad_2 = 0
        kid_2_DP_check = kid_2_s[2]
        if kid_2_DP_check is ".":
            kid_2_DP = 0
            kid_2_ab_1 = 0
            kid_2_ab_2 = 0
        else:
            kid_2_DP = int(kid_2_DP_check)
            if kid_2_DP == 0:
                kid_2_ab_1 = 0
                kid_2_ab_2 = 0
            else:
                kid_2_ab_1 = kid_2_ad_1 / float(kid_2_DP)
                kid_2_ab_2 = kid_2_ad_2 / float(kid_2_DP)
        kid_2_GQ_check = kid_2_s[3]
        if kid_2_GQ_check is ".":
            kid_2_GQ = 0
        else:
            kid_2_GQ = int(kid_2_GQ_check)

        # Getting info on kid nr 3, GT/DP/GQ.
        kid_3_s = spl[10].split(":")
        kid_3 = kid_3_s[0]
        kid_3_ad = kid_3_s[1]
        # Autosomes and Scaffold.
        if len(kid_3) > 1:
            kid_3_1 = list(kid_3)[0]
            kid_3_ad_1 = float(kid_3_ad.split(",")[0])
            kid_3_2 = list(kid_3)[2]
            kid_3_ad_2 = float(kid_3_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_3_1 = kid_3
            kid_3_2 = kid_3
            kid_3_ad_1 = 0
            kid_3_ad_2 = 0
        kid_3_DP_check = kid_3_s[2]
        if kid_3_DP_check is ".":
            kid_3_DP = 0
            kid_3_ab_1 = 0
            kid_3_ab_2 = 0
        else:
            kid_3_DP = int(kid_3_DP_check)
            if kid_3_DP == 0:
                kid_3_ab_1 = 0
                kid_3_ab_2 = 0
            else:
                kid_3_ab_1 = kid_3_ad_1 / float(kid_3_DP)
                kid_3_ab_2 = kid_3_ad_2 / float(kid_3_DP)
        kid_3_GQ_check = kid_3_s[3]
        if kid_3_GQ_check is ".":
            kid_3_GQ = 0
        else:
            kid_3_GQ = int(kid_3_GQ_check)

        # Getting info on kid nr 4, GT/DP/GQ.
        kid_4_s = spl[10].split(":")
        kid_4 = kid_4_s[0]
        kid_4_ad = kid_4_s[1]
        # Autosomes and Scaffold.
        if len(kid_4) > 1:
            kid_4_1 = list(kid_4)[0]
            kid_4_ad_1 = float(kid_4_ad.split(",")[0])
            kid_4_2 = list(kid_4)[2]
            kid_4_ad_2 = float(kid_4_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_4_1 = kid_4
            kid_4_2 = kid_4
            kid_4_ad_1 = 0
            kid_4_ad_2 = 0
        kid_4_DP_check = kid_4_s[2]
        if kid_4_DP_check is ".":
            kid_4_DP = 0
            kid_4_ab_1 = 0
            kid_4_ab_2 = 0
        else:
            kid_4_DP = int(kid_4_DP_check)
            if kid_4_DP == 0:
                kid_4_ab_1 = 0
                kid_4_ab_2 = 0
            else:
                kid_4_ab_1 = kid_4_ad_1 / float(kid_4_DP)
                kid_4_ab_2 = kid_4_ad_2 / float(kid_4_DP)
        kid_4_GQ_check = kid_4_s[3]
        if kid_4_GQ_check is ".":
            kid_4_GQ = 0
        else:
            kid_4_GQ = int(kid_4_GQ_check)

        # Getting info on kid nr 5, GT/DP/GQ.
        kid_5_s = spl[10].split(":")
        kid_5 = kid_5_s[0]
        kid_5_ad = kid_5_s[1]
        # Autosomes and Scaffold.
        if len(kid_5) > 1:
            kid_5_1 = list(kid_5)[0]
            kid_5_ad_1 = float(kid_5_ad.split(",")[0])
            kid_5_2 = list(kid_5)[2]
            kid_5_ad_2 = float(kid_5_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_5_1 = kid_5
            kid_5_2 = kid_5
            kid_5_ad_1 = 0
            kid_5_ad_2 = 0
        kid_5_DP_check = kid_5_s[2]
        if kid_5_DP_check is ".":
            kid_5_DP = 0
            kid_5_ab_1 = 0
            kid_5_ab_2 = 0
        else:
            kid_5_DP = int(kid_5_DP_check)
            if kid_5_DP == 0:
                kid_5_ab_1 = 0
                kid_5_ab_2 = 0
            else:
                kid_5_ab_1 = kid_5_ad_1 / float(kid_5_DP)
                kid_5_ab_2 = kid_5_ad_2 / float(kid_5_DP)
        kid_5_GQ_check = kid_5_s[3]
        if kid_5_GQ_check is ".":
            kid_5_GQ = 0
        else:
            kid_5_GQ = int(kid_5_GQ_check)

        # Getting info on kid nr 6, GT/DP/GQ.
        kid_6_s = spl[10].split(":")
        kid_6 = kid_6_s[0]
        kid_6_ad = kid_6_s[1]
        # Autosomes and Scaffold.
        if len(kid_6) > 1:
            kid_6_1 = list(kid_6)[0]
            kid_6_ad_1 = float(kid_6_ad.split(",")[0])
            kid_6_2 = list(kid_6)[2]
            kid_6_ad_2 = float(kid_6_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_6_1 = kid_6
            kid_6_2 = kid_6
            kid_6_ad_1 = 0
            kid_6_ad_2 = 0
        kid_6_DP_check = kid_6_s[2]
        if kid_6_DP_check is ".":
            kid_6_DP = 0
            kid_6_ab_1 = 0
            kid_6_ab_2 = 0
        else:
            kid_6_DP = int(kid_6_DP_check)
            if kid_6_DP == 0:
                kid_6_ab_1 = 0
                kid_6_ab_2 = 0
            else:
                kid_6_ab_1 = kid_6_ad_1 / float(kid_6_DP)
                kid_6_ab_2 = kid_6_ad_2 / float(kid_6_DP)
        kid_6_GQ_check = kid_6_s[3]
        if kid_6_GQ_check is ".":
            kid_6_GQ = 0
        else:
            kid_6_GQ = int(kid_6_GQ_check)

        # Getting info on kid nr 7, GT/DP/GQ.
        kid_7_s = spl[10].split(":")
        kid_7 = kid_7_s[0]
        kid_7_ad = kid_7_s[1]
        # Autosomes and Scaffold.
        if len(kid_7) > 1:
            kid_7_1 = list(kid_7)[0]
            kid_7_ad_1 = float(kid_7_ad.split(",")[0])
            kid_7_2 = list(kid_7)[2]
            kid_7_ad_2 = float(kid_7_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_7_1 = kid_7
            kid_7_2 = kid_7
            kid_7_ad_1 = 0
            kid_7_ad_2 = 0
        kid_7_DP_check = kid_7_s[2]
        if kid_7_DP_check is ".":
            kid_7_DP = 0
            kid_7_ab_1 = 0
            kid_7_ab_2 = 0
        else:
            kid_7_DP = int(kid_7_DP_check)
            if kid_7_DP == 0:
                kid_7_ab_1 = 0
                kid_7_ab_2 = 0
            else:
                kid_7_ab_1 = kid_7_ad_1 / float(kid_7_DP)
                kid_7_ab_2 = kid_7_ad_2 / float(kid_7_DP)
        kid_7_GQ_check = kid_7_s[3]
        if kid_7_GQ_check is ".":
            kid_7_GQ = 0
        else:
            kid_7_GQ = int(kid_7_GQ_check)

        # Getting info on kid nr 8, GT/DP/GQ.
        kid_8_s = spl[10].split(":")
        kid_8 = kid_8_s[0]
        kid_8_ad = kid_8_s[1]
        # Autosomes and Scaffold.
        if len(kid_8) > 1:
            kid_8_1 = list(kid_8)[0]
            kid_8_ad_1 = float(kid_8_ad.split(",")[0])
            kid_8_2 = list(kid_8)[2]
            kid_8_ad_2 = float(kid_8_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_8_1 = kid_8
            kid_8_2 = kid_8
            kid_8_ad_1 = 0
            kid_8_ad_2 = 0
        kid_8_DP_check = kid_8_s[2]
        if kid_8_DP_check is ".":
            kid_8_DP = 0
            kid_8_ab_1 = 0
            kid_8_ab_2 = 0
        else:
            kid_8_DP = int(kid_8_DP_check)
            if kid_8_DP == 0:
                kid_8_ab_1 = 0
                kid_8_ab_2 = 0
            else:
                kid_8_ab_1 = kid_8_ad_1 / float(kid_8_DP)
                kid_8_ab_2 = kid_8_ad_2 / float(kid_8_DP)
        kid_8_GQ_check = kid_8_s[3]
        if kid_8_GQ_check is ".":
            kid_8_GQ = 0
        else:
            kid_8_GQ = int(kid_8_GQ_check)

        # Getting info on kid nr 9, GT/DP/GQ.
        kid_9_s = spl[10].split(":")
        kid_9 = kid_9_s[0]
        kid_9_ad = kid_9_s[1]
        # Autosomes and Scaffold.
        if len(kid_9) > 1:
            kid_9_1 = list(kid_9)[0]
            kid_9_ad_1 = float(kid_9_ad.split(",")[0])
            kid_9_2 = list(kid_9)[2]
            kid_9_ad_2 = float(kid_9_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_9_1 = kid_9
            kid_9_2 = kid_9
            kid_9_ad_1 = 0
            kid_9_ad_2 = 0
        kid_9_DP_check = kid_9_s[2]
        if kid_9_DP_check is ".":
            kid_9_DP = 0
            kid_9_ab_1 = 0
            kid_9_ab_2 = 0
        else:
            kid_9_DP = int(kid_9_DP_check)
            if kid_9_DP == 0:
                kid_9_ab_1 = 0
                kid_9_ab_2 = 0
            else:
                kid_9_ab_1 = kid_9_ad_1 / float(kid_9_DP)
                kid_9_ab_2 = kid_9_ad_2 / float(kid_9_DP)
        kid_9_GQ_check = kid_9_s[3]
        if kid_9_GQ_check is ".":
            kid_9_GQ = 0
        else:
            kid_9_GQ = int(kid_9_GQ_check)

        # Getting info on kid nr 10, GT/DP/GQ.
        kid_10_s = spl[10].split(":")
        kid_10 = kid_10_s[0]
        kid_10_ad = kid_10_s[1]
        # Autosomes and Scaffold.
        if len(kid_10) > 1:
            kid_10_1 = list(kid_10)[0]
            kid_10_ad_1 = float(kid_10_ad.split(",")[0])
            kid_10_2 = list(kid_10)[2]
            kid_10_ad_2 = float(kid_10_ad.split(",")[1])
        # Mitochondrium.
        else:
            kid_10_1 = kid_10
            kid_10_2 = kid_10
            kid_10_ad_1 = 0
            kid_10_ad_2 = 0
        kid_10_DP_check = kid_10_s[2]
        if kid_10_DP_check is ".":
            kid_10_DP = 0
            kid_10_ab_1 = 0
            kid_10_ab_2 = 0
        else:
            kid_10_DP = int(kid_10_DP_check)
            if kid_10_DP == 0:
                kid_10_ab_1 = 0
                kid_10_ab_2 = 0
            else:
                kid_10_ab_1 = kid_10_ad_1 / float(kid_10_DP)
                kid_10_ab_2 = kid_10_ad_2 / float(kid_10_DP)
        kid_10_GQ_check = kid_10_s[3]
        if kid_10_GQ_check is ".":
            kid_10_GQ = 0
        else:
            kid_10_GQ = int(kid_10_GQ_check)

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

        # Loops below check whether either of two alleles in kids can be found in parents and whether parents and
        # kids DP and GQ are high enough (according to treshold set in the beginning of the file). If all these
        # conditions are met, the check variable is changed into True for particular kid.

        if (((kid_1_1 not in father) and (kid_1_1 not in mother) and (kid_1_1 is not ".") and (0.4 < kid_1_ab_1 > 0.6)) or
            ((kid_1_2 not in father) and (kid_1_2 not in mother) and (kid_1_2 is not ".") and (0.4 < kid_1_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                f1DPd <= kid_1_DP <= f1DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_1_GQ >= GQ:
            kid_1_check = True
        if (((kid_2_1 not in father) and (kid_2_1 not in mother) and (kid_2_1 is not ".") and (0.4 < kid_2_ab_1 > 0.6)) or
            ((kid_2_2 not in father) and (kid_2_2 not in mother) and (kid_2_2 is not ".") and (0.4 < kid_2_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                f2DPd <= kid_2_DP <= f2DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_2_GQ >= GQ:
            kid_2_check = True
        if (((kid_3_1 not in father) and (kid_3_1 not in mother) and (kid_3_1 is not ".") and (0.4 < kid_3_ab_1 > 0.6)) or
            ((kid_3_2 not in father) and (kid_3_2 not in mother) and (kid_3_2 is not ".") and (0.4 < kid_3_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                f3DPd <= kid_3_DP <= f3DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_3_GQ >= GQ:
            kid_3_check = True
        if (((kid_4_1 not in father) and (kid_4_1 not in mother) and (kid_4_1 is not ".") and (0.4 < kid_4_ab_1 > 0.6)) or
            ((kid_4_2 not in father) and (kid_4_2 not in mother) and (kid_4_2 is not ".") and (0.4 < kid_4_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                f4DPd <= kid_4_DP <= f4DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_4_GQ >= GQ:
            kid_4_check = True
        if (((kid_5_1 not in father) and (kid_5_1 not in mother) and (kid_5_1 is not ".") and (0.4 < kid_5_ab_1 > 0.6)) or
            ((kid_5_2 not in father) and (kid_5_2 not in mother) and (kid_5_2 is not ".") and (0.4 < kid_5_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                j1DPd <= kid_5_DP <= j1DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_5_GQ >= GQ:
            kid_5_check = True
        if (((kid_6_1 not in father) and (kid_6_1 not in mother) and (kid_6_1 is not ".") and (0.4 < kid_6_ab_1 > 0.6)) or
            ((kid_6_2 not in father) and (kid_6_2 not in mother) and (kid_6_2 is not ".") and (0.4 < kid_6_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                j2DPd <= kid_6_DP <= j2DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_6_GQ >= GQ:
            kid_6_check = True
        if (((kid_7_1 not in father) and (kid_7_1 not in mother) and (kid_7_1 is not ".") and (0.4 < kid_7_ab_1 > 0.6)) or
            ((kid_7_2 not in father) and (kid_7_2 not in mother) and (kid_7_2 is not ".") and (0.4 < kid_7_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                j3DPd <= kid_7_DP <= j3DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_7_GQ >= GQ:
            kid_7_check = True
        if (((kid_8_1 not in father) and (kid_8_1 not in mother) and (kid_8_1 is not ".") and (0.4 < kid_8_ab_1 > 0.6)) or
            ((kid_8_2 not in father) and (kid_8_2 not in mother) and (kid_8_2 is not ".") and (0.4 < kid_8_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                j4DPd <= kid_8_DP <= j4DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_8_GQ >= GQ:
            kid_8_check = True
        if (((kid_9_1 not in father) and (kid_9_1 not in mother) and (kid_9_1 is not ".") and (0.4 < kid_9_ab_1 > 0.6)) or
            ((kid_9_2 not in father) and (kid_9_2 not in mother) and (kid_9_2 is not ".") and (0.4 < kid_9_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                m1DPd <= kid_9_DP <= m1DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_9_GQ >= GQ:
            kid_9_check = True
        if (((kid_10_1 not in father) and (kid_10_1 not in mother) and (kid_10_1 is not ".") and (0.4 < kid_10_ab_1 > 0.6)) or
            ((kid_10_2 not in father) and (kid_10_2 not in mother) and (kid_10_2 is not ".") and (0.4 < kid_10_ab_2 > 0.6))) and \
                aDPd <= father_DP <= aDPu and \
                oDPd <= mother_DP <= oDPu and \
                m2DPd <= kid_10_DP <= m2DPu and \
                father_GQ >= GQ and mother_GQ >= GQ and kid_10_GQ >= GQ:
            kid_10_check = True

        # All kids check values are collected in a list.
        kids_check = [kid_1_check, kid_2_check, kid_3_check, kid_4_check, kid_5_check,
                      kid_6_check, kid_7_check, kid_8_check, kid_9_check, kid_10_check]

        # If any kid is marked True (as explained above), the variant is printed into the output file.
        if any(kids_check) and \
                FS <= 60 and \
                MQ >= 40 and \
                MQRankSum >= -12.5 and \
                ReadPosRankSum >= -8 and \
                SOR >= 3 and \
                QUAL_DP >= 2 and \
                INFO_check is True and \
                parents_check is True:
            with open(file_out, 'a') as f:
                print(variant, file=f, end="")
        else:
            with open(trash, 'a') as f:
                print(variant, file=f, end="")

# Input file is closed here and the script ends.
original_vcf.close()

print("De-novo mutations found.")
