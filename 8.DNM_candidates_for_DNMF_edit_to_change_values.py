# This script produces DNMF-ready input file of candidate DNMs.
import sys

in_put = sys.argv[1]
out_put = sys.argv[2]

print("Hello!")
print("Let's start!")

original_vcf = open(in_put, 'r')
lines = original_vcf.readlines()

# Here insert your minimal(d) and maximal(u) dp values and offspring names.
d = [23, 16, 19, 15, 20, 15, 17, 21, 18, 23]
u = [90, 62, 74, 56, 82, 40, 70, 84, 72, 94]
names = ["7f1", "7f2", "7f3", "7f4", "7j1", "7j2", "7j3", "7j4", "7m1", "7m2"]
GQ = 70

for v, variant in enumerate(lines, start=0):

    spl = variant.split("\t")

    chromosome = spl[0]
    loc = spl[1]
    a = spl[9]
    f1 = spl[10]
    f2 = spl[11]
    f3 = spl[12]
    f4 = spl[13]
    j1 = spl[14]
    j2 = spl[15]
    j3 = spl[16]
    j4 = spl[17]
    m1 = spl[18]
    m2 = spl[19]
    o = spl[20]

    father_dp = int(a.split(":")[2])
    father_gq = int(a.split(":")[3])
    father_gt = a.split(":")[0]
    a_gt = list(father_gt)

    mother_dp = int(o.split(":")[2])
    mother_gq = int(o.split(":")[3])
    mother_gt = o.split(":")[0]
    o_gt = list(mother_gt)

    kids = [f1, f2, f3, f4, j1, j2, j3, j4, m1, m2]

    for k, kid in enumerate(kids, start=0):
        k_gt = kid.split(":")[0]
        k_1 = list(k_gt)[0]
        k_2 = list(k_gt)[2]
        k_dp = int(kid.split(":")[2])
        k_gq = int(kid.split(":")[3])
        k_check = False

        if (((k_1 not in a_gt) and (k_1 not in o_gt) and k_1 is not ".") or
            ((k_2 not in a_gt) and (k_2 not in o_gt) and k_2 is not ".")) and \
                d[k] <= k_dp <= u[k] and k_gq >= GQ:
            k_check = True

        if k_check:
            with open(out_put, mode='a') as x:
                print(names[k], chromosome, loc, sep=',', file=x, end="\n")

original_vcf.close()

print("End")
