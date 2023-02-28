from typing import List, TextIO
import sys

file_in = sys.argv[1]
fam = sys.argv[2]
chrom = sys.argv[3]

print("Hello!")
print("We are running Heterozygosity SCRIPT")
print("Working...")

# First, let's load vcf file.
original_vcf = open(file_in, 'r')
lines = original_vcf.readlines()

Heterozygosity1 = 0
Count1 = 0
Heterozygosity2 = 0
Count2 = 0
Heterozygosity3 = 0
Count3 = 0
Heterozygosity4 = 0
Count4 = 0
Heterozygosity5 = 0
Count5 = 0
Heterozygosity6 = 0
Count6 = 0
Heterozygosity7 = 0
Count7 = 0
Heterozygosity8 = 0
Count8 = 0
Heterozygosity9 = 0
Count9 = 0
Heterozygosity10 = 0
Count10 = 0
Heterozygosity11 = 0
Count11 = 0
Heterozygosity12 = 0
Count12 = 0

# Loop starts here.
for v, variant in enumerate(lines, start=0):

    # Splitting variant into fields.
    spl = variant.split("\t")
    # Getting info on father, GT/DP/GQ.
    indv1 = spl[0].split(":")[0]
    indv2 = spl[1].split(":")[0]
    indv3 = spl[2].split(":")[0]
    indv4 = spl[3].split(":")[0]
    indv5 = spl[4].split(":")[0]
    indv6 = spl[5].split(":")[0]
    indv7 = spl[6].split(":")[0]
    indv8 = spl[7].split(":")[0]
    indv9 = spl[8].split(":")[0]
    indv10 = spl[9].split(":")[0]
    indv11 = spl[10].split(":")[0]
    indv12 = spl[11].split(":")[0]

    if indv1 in {"1/0", "0/1",  "1|0", "0|1"}:
        Heterozygosity1 = Heterozygosity1 + 1
        Count1 = Count1 + 1
    elif indv1 in {"0/0", "0|0"}:
        Count1 = Count1 + 1

    if indv2 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity2 = Heterozygosity2 + 1
        Count2 = Count2 + 1
    elif indv2 in {"0/0", "0|0"}:
        Count2 = Count2 + 1

    if indv3 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity3 = Heterozygosity3 + 1
        Count3 = Count3 + 1
    elif indv3 in {"0/0", "0|0"}:
        Count3 = Count3 + 1

    if indv4 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity4 = Heterozygosity4 + 1
        Count4 = Count4 + 1
    elif indv4 in {"0/0", "0|0"}:
        Count4 = Count4 + 1

    if indv5 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity5 = Heterozygosity5 + 1
        Count5 = Count5 + 1
    elif indv5 in {"0/0", "0|0"}:
        Count5 = Count5 + 1

    if indv6 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity6 = Heterozygosity6 + 1
        Count6 = Count6 + 1
    elif indv6 in {"0/0", "0|0"}:
        Count6 = Count6 + 1

    if indv7 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity7 = Heterozygosity7 + 1
        Count7 = Count7 + 1
    elif indv7 in {"0/0", "0|0"}:
        Count7 = Count7 + 1

    if indv8 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity8 = Heterozygosity8 + 1
        Count8 = Count8 + 1
    elif indv8 in {"0/0", "0|0"}:
        Count8 = Count8 + 1

    if indv9 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity9 = Heterozygosity9 + 1
        Count9 = Count9 + 1
    elif indv9 in {"0/0", "0|0"}:
        Count9 = Count9 + 1

    if indv10 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity10 = Heterozygosity10 + 1
        Count10 = Count10 + 1
    elif indv10 in {"0/0", "0|0"}:
        Count10 = Count10 + 1

    if indv11 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity11 = Heterozygosity11 + 1
        Count11 = Count11 + 1
    elif indv11 in {"0/0", "0|0"}:
        Count11 = Count11 + 1

    if indv12 in {"1/0", "0/1", "1|0", "0|1"}:
        Heterozygosity12 = Heterozygosity12 + 1
        Count12 = Count12 + 1
    elif indv12 in {"0/0", "0|0"}:
        Count12 = Count12 + 1

print("Chromosome:")
print(chrom)
print("Family:")
print(fam)
print("\n")

print("INDIVIDUAL 1")
print("Heterozygotes: ", Heterozygosity1)
print("Total sites: ", Count1)
print("Mean heterozygosity: ", Heterozygosity1/Count1)
print("\n")

print("INDIVIDUAL 2")
print("Heterozygotes: ", Heterozygosity2)
print("Total sites: ", Count2)
print("Mean heterozygosity: ", Heterozygosity2/Count2)
print("\n")

print("INDIVIDUAL 3")
print("Heterozygotes: ", Heterozygosity3)
print("Total sites: ", Count3)
print("Mean heterozygosity: ", Heterozygosity3/Count3)
print("\n")

print("INDIVIDUAL 4")
print("Heterozygotes: ", Heterozygosity4)
print("Total sites: ", Count4)
print("Mean heterozygosity: ", Heterozygosity4/Count4)
print("\n")

print("INDIVIDUAL 5")
print("Heterozygotes: ", Heterozygosity5)
print("Total sites: ", Count5)
print("Mean heterozygosity: ", Heterozygosity5/Count5)
print("\n")

print("INDIVIDUAL 6")
print("Heterozygotes: ", Heterozygosity6)
print("Total sites: ", Count6)
print("Mean heterozygosity: ", Heterozygosity6/Count6)
print("\n")

print("INDIVIDUAL 7")
print("Heterozygotes: ", Heterozygosity7)
print("Total sites: ", Count7)
print("Mean heterozygosity: ", Heterozygosity7/Count7)
print("\n")

print("INDIVIDUAL 8")
print("Heterozygotes: ", Heterozygosity8)
print("Total sites: ", Count8)
print("Mean heterozygosity: ", Heterozygosity8/Count8)
print("\n")

print("INDIVIDUAL 9")
print("Heterozygotes: ", Heterozygosity9)
print("Total sites: ", Count9)
print("Mean heterozygosity: ", Heterozygosity9/Count9)
print("\n")

print("INDIVIDUAL 10")
print("Heterozygotes: ", Heterozygosity10)
print("Total sites: ", Count10)
print("Mean heterozygosity: ", Heterozygosity10/Count10)
print("\n")

print("INDIVIDUAL 11")
print("Heterozygotes: ", Heterozygosity11)
print("Total sites: ", Count11)
print("Mean heterozygosity: ", Heterozygosity11/Count11)
print("\n")

print("INDIVIDUAL 12")
print("Heterozygotes: ", Heterozygosity12)
print("Total sites: ", Count12)
print("Mean heterozygosity: ", Heterozygosity12/Count12)
print("\n")

# Input file is closed here and the script ends.
original_vcf.close()
