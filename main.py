import argparse
from Bio.Seq import Seq

# Read inputs provided by user
parser = argparse.ArgumentParser()
parser.add_argument('--sequence')
parser.add_argument('--rc')
args = parser.parse_args()

dna = Seq(args.sequence)

# Check if user wanted the reverse compliment
if args.rc == 'yes':
    dna = dna.reverse_complement()

rna = dna.transcribe()

print('DNA: ' + dna)
print('RNA: ' + rna)

# Check if user wants the protein sequence
if args.translate == 'yes':
    print('Protein (translated from RNA to STOP): ' + rna.translate(to_stop=True))
