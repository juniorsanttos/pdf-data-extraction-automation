import re
import os
import pdfplumber

dict_infos = {
    "Municipio": r"(?:MUNICIPIO|Município)\s*:\s*(.*?)(?=Long\.|Latitude|Localidade|\n|$)",
    "Localidade":r"(?:Localidade\s*|LOCALIDADE)\s*:\s*(.*?)(?=\s{2,}|\n|Prof\.|util\(m\)|$)",
    "Longitude":r"(?:Long\.\s*\(w\)|COORDENADA\s*E/O)\s*:\s*(.*?)(?=COORDENADA\s*N/S\s*:\S*|Localidade|Lat|Município|\n|$)",
    "Latitude":r"(?:Latitude\s*\(s\)|COORDENADA\s*N/S)\s*:(.*?)(?=COORDENADA\s*E/O|Long\.|Município|\n|$)"
}


def arquivos(path):
    files = os.listdir(path)
    return files

def extrair_dados(nome_pdf):
    #Lendo conteudo da pagina
    with pdfplumber.open(nome_pdf) as pdf:
        pagina = pdf.pages[0] #Começa da primeira pagina 
        texto = pagina.extract_text() #pega o conteudo da pagina
        #print(texto)

        results = {}

        for k, info in dict_infos.items(): # Para cada info do dicionario
            info_important = re.search(info, texto, re.DOTALL | re.IGNORECASE)

            if info_important:
                results[k] = info_important.group(1).replace("\n","") #Retorna apenas a info
                
            
            else:
                results[k] = None

        return results

def write_csv(csv,list):
    with open(csv, "a") as csv:
        for k, info in list.items(): #Para cada info
            print("Escrito: ", info) 

            csv.write(f"{info};")   #Escreve no arquivo
        
        csv.write("\n") #Pula linha
