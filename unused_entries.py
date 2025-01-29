import os
import re

# Path to your LaTeX project
project_path = "/home/worfran/Documents/Latex/Tesis-reactores/"

# Function to extract citation keys from .aux file
def extract_citations(aux_file):
    citations = set()
    with open(aux_file, 'r') as file:
        for line in file:
            match = re.search(r'\\citation{(.+?)}', line)
            if match:
                citations.update(match.group(1).split(','))
    return citations

# Function to extract entries from .bib files
def extract_bib_entries(bib_file):
    entries = set()
    with open(bib_file, 'r') as file:
        for line in file:
            match = re.search(r'@.+?{(.+?),', line)
            if match:
                entries.add(match.group(1))
    return entries

# Extract citations from .aux file
aux_file = os.path.join(project_path, "Tesis_Reactores.aux")
citations = extract_citations(aux_file)

# Extract entries from all .bib files
bib_files = [
    "Anexos/BibtexAnexos.bib",
    "Kap1/BibtexChap1.bib",
    "Kap2/BibtexChap2.bib",
    "Kap3/BibtexChap3.bib",
    "Kap4/BibtexChap4.bib",
    "Kap5/BibtexChap5.bib",
    "Kap6/BibtexChap6.bib",
    "Kap7/BibtexChap7.bib",
    "Kap8/BibtexChap8.bib"
]

all_entries = set()
for bib_file in bib_files:
    bib_path = os.path.join(project_path, bib_file)
    all_entries.update(extract_bib_entries(bib_path))

# Find unused entries
unused_entries = all_entries - citations

# Print unused entries
print("Unused entries:")
for entry in unused_entries:
    print(entry)