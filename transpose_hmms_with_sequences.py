########################################
### transpose_hmms_with_sequences.py ###
########################################
# Author: Samuel Aroney
# Trawl through extracted sequences matching target HMMs
# Extract these into separate files for each HMM

# input [GENOME ID]_protein.fam.faa:
# >[SEQUENCE ID]<space>[RANDOM TEXT]
# GENE SEQUENCE...

# input [GENOME ID]_protein.fam:
# [SEQUENCE ID]<tab>[HMM ID]

# intended output HMM file [PACKAGE NAME].faa:
# >[GENOME ID]-[PACKAGE NAME]
# GENE SEQUENCE...



# Manual testing
# python transpose_hmms_with_sequences.py \
#     --input-fasta ./test/GB_GCA_000091165.1_protein.fam.faa \
#     --hmm-seq ./test/GB_GCA_000091165.1_protein.fam \
#     --hmm-spkg ./hmms_and_names \
#     --output ./test_output/

# Manual testing parallel
# find test/ |
# grep fam$ |
# parallel \
# python transpose_hmms_with_sequences.py \
#     --input-fasta {}.faa \
#     --hmm-seq {} \
#     --hmm-spkg ./hmms_and_names \
#     --output ./test_output/



import argparse
import logging
import csv
import os
import re
from Bio import SeqIO


parser = argparse.ArgumentParser(description='Extract sequences into separate HMM files.')
parser.add_argument('--input-fasta', type=str, metavar='<INPUT FASTA>', help='path to sequence file')
parser.add_argument('--hmm-seq', type=str, metavar='<HMM SEQ LIST>', help='list of HMMs with sequences')
parser.add_argument('--hmm-spkg', type=str, metavar='<HMM SPKG LIST>', help='list of HMMs with SingleM package')
parser.add_argument('--output', type=str, metavar='<OUTPUT>', help='path to output directory')

args = parser.parse_args()
input_path = getattr(args, 'input_fasta')
genome_id = re.findall(r'(.*)_protein', os.path.basename(input_path))[0]
HMM_seq_list = getattr(args, 'hmm_seq')
HMM_id_list = getattr(args, 'hmm_spkg')
NEW_VERSION_HMM_COLUMN = "r202"
NEW_VERSION_NAME_COLUMN = "r202_name"
output_dir = getattr(args, 'output')

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')


logging.info("Creating HMM package-match and sequence-match dictionaries")
with open(HMM_seq_list) as file:
    hmms = csv.reader(file, delimiter="\t")
    Seq_HMM = {line[0]:line[1] for line in hmms}

with open(HMM_id_list) as file:
    hmms = csv.DictReader(file, delimiter="\t")
    HMM_spkg = {line[NEW_VERSION_HMM_COLUMN]:line[NEW_VERSION_NAME_COLUMN] for line in hmms}

HMM_output = {spkg:{} for spkg in set(HMM_spkg.values())}


logging.info(f"Load fasta file from {input_path}")
for sequence in SeqIO.parse(input_path, "fasta"):
    HMM_ID = Seq_HMM[sequence.id]
    spkg = HMM_spkg[HMM_ID]
    HMM_output[spkg] = sequence.seq
    

example_output_file = os.path.join(output_dir, list(HMM_output.keys())[0] + '.faa')
logging.info(f"Save matching sequences in spkg files e.g. {example_output_file}")
for spkg in HMM_output.keys():
    if HMM_output[spkg] != {}:
        with open(os.path.join(output_dir, spkg + ".faa"), 'a') as output_file:
            # print(f">{genome_id}-{spkg}")
            # print(HMM_output[spkg])
            output_file.write(f">{genome_id}-{spkg}\n")
            output_file.write(f"{HMM_output[spkg]}\n")






