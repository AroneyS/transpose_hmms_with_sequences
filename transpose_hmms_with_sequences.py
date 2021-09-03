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
# > [GENOME ID]-[PACKAGE NAME]
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
import csv
import os

import pdb


parser = argparse.ArgumentParser(description='Extract sequences into separate HMM files.')
parser.add_argument('--input-fasta', type=str, metavar='<INPUT FASTA>', help='path to sequence file')
parser.add_argument('--hmm-seq', type=str, metavar='<HMM SEQ LIST>', help='list of HMMs with sequences')
parser.add_argument('--hmm-spkg', type=str, metavar='<HMM SPKG LIST>', help='list of HMMs with SingleM package')
parser.add_argument('--output', type=str, metavar='<OUTPUT>', help='path to output directory')

args = parser.parse_args()
input_path = getattr(args, 'input_fasta')
HMM_seq_list = getattr(args, 'hmm_seq')
HMM_id_list = getattr(args, 'hmm_spkg')
NEW_VERSION_HMM_COLUMN = "r202"
NEW_VERSION_NAME_COLUMN = "r202_name"
output_dir = getattr(args, 'output')

with open(HMM_seq_list) as file:
    hmms = csv.reader(file, delimiter="\t")
    Seq_HMM = {line[0]:line[1] for line in hmms}

with open(HMM_id_list) as file:
    hmms = csv.DictReader(file, delimiter="\t")
    HMM_spkg = {line[NEW_VERSION_HMM_COLUMN]:line[NEW_VERSION_NAME_COLUMN] for line in hmms}

os.listdir(output_dir)


# Open fasta file and trawl through each sequence
# Use Seq_HMM to get HMM name from sequence ID
# Use HMM_spkg to get spkg name from HMM name
# Get genome ID from filename
# Append sequence to spkg name file with ID of genome ID and spkg name


#pdb.set_trace()



