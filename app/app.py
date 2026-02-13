from app.pdf_utils import *
import os
import shutil

files = arquivos("Entrada")
Entrada = "Entrada"
Saida = "Processados"

for file in files:

    origem_file = os.path.join(Entrada, file)
    
    infos = extrair_dados(f"Entrada/{file}")
    write_csv("resultado.csv",infos)

    destine_file = os.path.join(Saida, file)
    shutil.move(origem_file, destine_file)