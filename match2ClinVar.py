# imports go here

class VarPosition():
    # Class to track variant position.
    # Store minimum necessary information to define a variant.

    def __init__(vcf_record):
        # initialize a VarPosition object

class ClinVarPosition(VarPosition):
    # Extend VarPosition to store information contained in a ClinVar VCF

    def __init__(self, vcf_record):
        # First does the VarPosition.__init__
        super(ClinVarPosition, self).__init__(vcf_record)
        # Then store additional ClinVar information

class GenVarPosition(VarPosition):
    # Extend VarPosition to store information contained in a single genome.

    def __init__(self, vcf_record):
        # First does the VarPosition.__init__
        super(VarPosition, self).__init(vcf_record)
        # Then store genotype data

def main():
    # Set up two file readers:
    # One for the ClinVar file, one for the genome data.
    # For now you can just use sys.argv[1], implement
    # flags later.

    # Create a loop where, each step, the file with
    # the earliest line "steps forward".

    # If both lines are at the same position, print them
    # both out as a "match", then advance both files.

if __name__ == "__main__":
    main()
