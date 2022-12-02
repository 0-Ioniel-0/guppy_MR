# This is done for one individual and one chromosome (to save time and resources). One needs to split g.vcf file. Provie script with indiviual's DP and GQ tresholds.

from typing import List, TextIO
import sys

# Getting input
minDP = int(sys.argv[1])
maxDP = int(sys.argv[2])
minGQ = int(sys.argv[3])
# Input
individual = sys.argv[4]
# Output
effective_sites = sys.argv[5]
# Header length
HD = int(sys.argv[6])

print("Hello!")
print("We're running effective sites finding script.")

# Opening input file
gvcf: TextIO = open(individual, 'r')
lines = gvcf.readlines()
count = 0

# Main loop writing effective sites to a new file
for s, site in enumerate(lines, start=0):

    if s > HD-1:

        # Splitting line into parts
        spl: List[str] = site.split("\t")

        info = spl[9]
        text = spl[8]
        info_spl = info.split(":")
        text_spl = text.split(":")
        info_len = len(info_spl)

        # Defining new function that searches whether site has a DP info
        def search(zbior, item):
            for i in range(len(zbior)):
                if zbior[i] == item:
                    return True
            return False

        # Finding DP and GQ values
        if search(text_spl, "DP"):

            # REF_HOMO
            if info_len == 5:
                dp = int(info_spl[1])
                gq = int(info_spl[2])

            # ALT
            else:
                dp = int(info_spl[2])
                gq = int(info_spl[3])

        # MISSING
        else:
            dp = 0
            gq = 0

        # Writing position/s into new file
        if gq >= minGQ and maxDP >= dp >= minDP:

        	with open(effective_sites, 'a') as g:
                    print(scaffold, file=g, end="\t")
                    print(pos, file=g, end="\n")
                    count = count + 1

print("End!")
print(individual)
print("Effective sites: ", count)

# Closing input file
gvcf.close()
