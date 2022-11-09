#!/usr/bin/env python3

import urllib.request
import sys
import xml.etree.ElementTree as ET

URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?dbfrom=sra&db=biosample&id="

# read in biosample accessions from a text file
biosample_accs = []
with open(sys.argv[1],"r") as in_accs_file:
    for line in in_accs_file.readlines():
        if line.strip():
            biosample_accs.append(line.strip())

# join the list of biosample accs with a comma for url formatting
biosample_accs_list = ",".join(biosample_accs)
    
# get the xml response from NCBI efetch
xml_response = urllib.request.urlopen(URL + biosample_accs_list)

# decode and parse XML response
xml_string = xml_response.read().decode("utf-8")
tree = ET.fromstring(xml_string)

# find the XML elements that have the IDs in them
biosample_ids = [element.text for element in tree.findall(".//Id[@db='BioSample']")]
sra_ids = [element.text for element in tree.findall(".//Id[@db='SRA']")]
zipped_out = zip(biosample_ids, sra_ids)

# write out and print the converted IDs to the command line
with open("./converted_accs.csv", "w") as out_accs:
    out_accs.write("BioSample_ID,SRA_ID\n")
    for acc in zipped_out:
        print(acc[0], "->", acc[1])
        out_accs.write(f"{acc[0]},{acc[1]}\n")

