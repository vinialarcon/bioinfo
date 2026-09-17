from Bio import SeqIO

caminho = "data/NC_001422.fasta"  # ajuste o nome se o arquivo baixou com outro nome

for registro in SeqIO.parse(caminho, "fasta"):
    print("ID:", registro.id)
    print("Descrição:", registro.description)
    print("Tamanho:", len(registro.seq))
    print("Primeiros 50 nucleotídeos:", registro.seq[:50])
