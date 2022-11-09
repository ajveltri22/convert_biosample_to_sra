# Purpose

This script converts NCBI BioSample accessions to thier corresponding NCBI SRA accesssions. It prints the conversions to the command line and to a file in the present directory: `converted_accs.csv`.

# Usage

The first argument is a text file of input accessions. See `biosample_input_accs.txt` for the format.

> `python3 ./convert_biosample_to_sra.py ./biosample_input_accs`

# Caveats
This will not work if there are multiple SRA accessions for a single BioSample accession. Should be easily fixable with some minor tweaks.

# Requirements

Python > 3.6