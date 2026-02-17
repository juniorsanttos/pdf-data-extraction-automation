from pdf_utils import *
import os
import shutil
from pathlib import Path

files = arquivos("Entrada")
entrada_path = Path("Entrada")
processados_Path = Path("Processados")

entrada_path.mkdir(exist_ok=True) #Caso não exista, crie a pasta "Entrada"
processados_Path.mkdir(exist_ok=True) #Caso não exista, crie a pasta "Processados"

if len(files) == 0: #Caso não tenha arquivos na pasta "Entrada"
    print("Não há arquivos na pasta")

else:
    for file in files:

        origem_file = entrada_path / file #Origem da pasta
        
        infos = extrair_dados(entrada_path / file)
        write_csv("resultado.csv",infos)

        destine_file = processados_Path / file #Destino final - "Processados"
        shutil.move(origem_file, destine_file) #Passa o arquivo da "Entrada" para os "Processados"