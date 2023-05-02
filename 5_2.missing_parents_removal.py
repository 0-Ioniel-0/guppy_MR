# FINDING MISSING PARENTS

import sys

file_in = sys.argv[1]
file_out = sys.argv[2]
# Parent 1 position in a VCF file
parent_1 = int(sys.argv[3])
# Parent 2 position in a VCF file
parent_2 = int(sys.argv[4])

print("Hello!")
print("We are running MISSING script")
print("Working...")

# First, let's load vcf file.
original_vcf = open(file_in, 'r')
lines = original_vcf.readlines()
missing_count = 0

# Loop starts here.
for v, variant in enumerate(lines, start=0):

    # Print header to the output file.
    if variant.startswith('#'):
        with open(file_out, 'a') as f:
            print(variant, file=f, end=" ")

    # Go through variants.
    else:
        # Splitting variant into fields.
        spl = variant.split("\t")

        # Getting info on first parent.
        A_s = spl[parent_1].split(":")
        A = str(A_s[0])
        # Getting info on second parent.
        B_s = spl[parent_2].split(":")
        B = str(B_s[0])

        if (A != "./." and A != ".") and (B != "./." or B != "."):
            with open(file_out, 'a') as f:
                print(variant, file=f, end="")
        else:
            missing_count = missing_count + 1

# Input file is closed here and the script ends.
original_vcf.close()

print("Missing parents found and removed.")
print("Number of missing sites:", missing_count)
