# Take genome fasta file with HMM matches and produce a HMM/spkg specific fasta file

## Inputs

### input [GENOME ID]_protein.fam.faa (fasta)

```
>[SEQUENCE ID]<space>[RANDOM TEXT]
GENE SEQUENCE...
```

### input [GENOME ID]_protein.fam (tsv)

```
[SEQUENCE ID]<tab>[HMM ID]
```

### input hmms_and_names (tsv)

Contains each [PACKAGE NAME] and their equivalent [HMM ID]

### input bacterial/archaeal taxonomy (tsv)

```
[GENOME ID]<tab>[taxonomy]
```

## Outputs

### intended output HMM file [PACKAGE NAME].faa (fasta)

```
>[GENOME ID]-[PACKAGE NAME]
GENE SEQUENCE...
```

### intended output taxonomy file [PACKAGE NAME]_taxonomy.tsv (tsv)

```
[GENOME ID]-[PACKAGE NAME]<tab>[taxonomy]
```

## Steps

1. Open `[GENOME ID]_protein.fam.faa` fasta file and trawl through each sequence
1. Use `[GENOME ID]_protein.fam` to get HMM name from sequence ID
1. Use `hmms_and_names` to get spkg name from HMM name
1. Get genome ID from fasta filename
1. Append sequence to `[spkg name].faa` file with ID composed of genome ID and spkg name
1. Find genome ID and taxonomy from bacteria or archaea taxonomy file
1. Append taxonomy to `[spkg name]_taxonomy.tsv` file with ID as above
