from Bio import SeqIO
manual = SeqIO.read("data/NC_001422.fasta", "fasta")
codigo = SeqIO.read("data/phix174_entrez.fasta", "fasta")

#Conta as linhas de cada arquivo, como você viu na tela
linhas_manual = sum(1 for linha in open("data/NC_001422.fasta"))
linhas_codigo = sum(1 for linha in open("data/phix174_entrez.fasta"))

print("Linhas no arquivo baixado à mão: ", linhas_manual)
print("Linhas no arquivo baixado pelo código: ", linhas_codigo)
print()
print("Bases no arquivo baixado à mão: ", len(manual.seq))
print("Bases no arquivo baixado pelo código: ", len(codigo.seq))
print()
print("As sequências são iguais? ", manual.seq == codigo.seq)