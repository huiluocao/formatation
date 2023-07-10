from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from BCBio import GFF

# Input files
gff_file = "gff/I003.gff3"
fasta_file = "contigs/contigs1/I003_contig100.fasta"

# Output file
gbk_file = "output.gbk"

# Read the FASTA records
fasta_records = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

# Read the GFF file
gff_records = GFF.parse(gff_file, base_dict=fasta_records)

# Add molecule_type annotation to each record
for record in gff_records:
    record.annotations["molecule_type"] = "DNA"
    print(record)

# Write the output GBK file
    with open(gbk_file, "a") as output_handle:
        SeqIO.write(record, output_handle, "genbank")
