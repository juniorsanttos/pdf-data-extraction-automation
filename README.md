# 📄PDF Data Extraction Automation
Automação em Python para extração de dados específicos de fichas de poço em PDF e geração automática de um arquivo CSV consolidado. 

Projeto desenvolvido para resolver uma dor real da engenharia civil, eliminando um processo manual repetitivo e demorado.

## 🎯 Problema
Profissionais de engenharia frequentemente tem que extrair manualmente informações de uma ficha de poço em formato de pdf.

Esse processo é: 
 - Repetitivo
 - Demorado
 - Cansativo
 - Propenso a erros

Este projeto tem como afinidade resolver essa dor automatizando totalmente esse processo!

## 🚀 Solução

O programa:

1.  Lê todos os arquivos PDF da pasta `Entrada`
    
2.  Extrai dados específicos utilizando:
    
    -   `pdfplumber` para leitura do PDF
        
    -   `regex` para captura precisa das informações
        
3.  Gera automaticamente um arquivo `.csv` consolidado
    
4.  Move os PDFs processados para a pasta `processados`

Tudo isso com apenas um comando.

## 🛠 Tecnologias Utilizadas

 - Python 3.12
 - pdfplumber
 - re (regex)
 - csv
 
 ## 📂 Estrutura Do Projeto

    pdf-data-extraction-automation/
    |
    ├── app/
    │ ├── app.py # Arquivo principal (ponto de entrada)
    │ ├── pdf_utils.py # Funções auxiliares para extração
    │
    ├── Entrada/ # PDFs a serem processados
    ├── Processados/ # PDFs já processados (Pasta criada automaticamente ao rodar script)
    │
    ├── requiriments.txt # Dependências do projeto
    ├── LICENSE 
    └── README.md
## ▶️ Como Executar 
1️⃣ Clone o repositório

    git clone https://github.com/seu-usuario/pdf-data-extraction-automation
    cd pdf-data-extraction-automation
 
###
2️⃣ Instale as dependências

    pip install -r requiriments.txt
 ### 
3️⃣ Execute o programa 

    python app/app.py
    
Pronto ✅  
Todos os PDFs da pasta `Entrada/` serão processados automaticamente.

##  📈 Benefícios

-   ⏱ Economia de tempo
    
-   📉 Redução de erro humano
    
-   🔁 Eliminação de tarefas repetitivas
    
-   📊 Dados organizados automaticamente em CSV
    
-   💼 Aplicação prática em engenharia civil
