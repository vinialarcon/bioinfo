from Bio import SeqIO

registro = SeqIO.read("data/phix174_entrez.fasta", "fasta")
dna = registro.seq

# Um trecho curto, só para caber na tela
trecho = dna[:30]

print("Fita original (5'->3'):", trecho)
print("Complemento:           ", trecho.complement())
print("Complemento reverso:   ", trecho.reverse_complement())
print()
print("Transcrito em RNA:     ", trecho.transcribe())
print("Traduzido em proteína: ", trecho.translate())
print()
print("--- Os três quadros de leitura ---")
print("Quadro 1:", dna[0:30].translate())
print("Quadro 2:", dna[1:31].translate())
print("Quadro 3:", dna[2:32].translate())

print()
print("--- Procurando quadros abertos no genoma inteiro ---")
print("Quadro | Paradas | Maior trecho sem parada (aminoácidos)")

for inicio in range(3):
    recorte = dna[inicio:]
    # corta o final para o comprimento virar múltiplo de 3
    recorte = recorte[:len(recorte) - len(recorte) % 3]
    proteina = str(recorte.translate())
    paradas = proteina.count("*")
    maior_trecho = max(len(pedaco) for pedaco in proteina.split("*"))
    print(f"   {inicio + 1}   |  {paradas:4}   |  {maior_trecho}")