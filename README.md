# bioinfo

Repositório de estudos e projetos de bioinformática.

## Projeto 1 — Análise de sequências com Biopython

Análise do genoma do bacteriófago phiX174 (accession `NC_001422.1`, 5.386 bases):
leitura de arquivos FASTA, download reprodutível via NCBI Entrez, cálculo de
conteúdo GC e visualização dos resultados.

**Status:** em andamento.

## Estrutura

```
.
├── data/              # sequências baixadas do NCBI (entrada)
├── results/           # gráficos e saídas geradas pelos scripts
├── 01_ler_fasta.py    # lê um FASTA e imprime ID, descrição e tamanho
└── .gitignore
```

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate      # Windows (PowerShell: .\venv\Scripts\Activate.ps1)
pip install biopython
python 01_ler_fasta.py
```

---

*README provisório — a versão final, com objetivo, método e resultados, é a tarefa do Módulo 1.6 da trilha.*
