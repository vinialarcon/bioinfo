from Bio import Entrez, SeqIO

# O NCBI exige que toda chamada se identifique. Troque pelo seu e-mail real.
Entrez.email = "alarconvini@gmail.com"

ACCESSION = "NC_001422.1"

# efetch = buscar um registro específico.
# db="nucleotide" → banco de sequências de DNA/RNA
# rettype="fasta" → formato desejado
# retmode="text"  → devolver como texto puro, não XML
with Entrez.efetch(db="nucleotide", id=ACCESSION, rettype="fasta", retmode="text") as handle:
    registro = SeqIO.read(handle, "fasta")

print("ID:", registro.id)
print("Descrição:", registro.description)
print("Tamanho:", len(registro.seq), "bases")

SeqIO.write(registro, "data/phix174_entrez.fasta", "fasta")
print("Arquivo salvo em data/phix174_entrez.fasta")