# FINDING MISSING PARENTS

from typing import List, TextIO
import sys

file_in = sys.argv[1]

print("Hello!")
print("We are running MISSING SCRIPT")
print("Working...")

# First, let's load vcf file.
original_vcf = open(file_in, 'r')
lines = original_vcf.readlines()

# Loop starts here.
for v, variant in enumerate(lines, start=0):

    # Header first.
    if variant.startswith('#'):
        with open(file_out, 'a') as f:
                print(variant, file=f, end=" ")

    # Now, main thing.
    else:

        # Splitting variant into fields.
        spl = variant.split("\t")

        # Getting info on father, GT/DP/GQ.
        Afather_s = spl[9].split(":")
        Afather = str(Afather_s[0])
        Bfather_s = spl[21].split(":")
        Bfather = str(Bfather_s[0])

        if Amother is  not "." and Afather is not "." and Bmother is not "." or Bfather is not ".":
            with open(file_out, 'a') as f:
                print(variant, file=f, end=" ")

# Input file is closed here and the script ends.
original_vcf.close()

print("Missing parents found.")
