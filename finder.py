import os
import re

def is_file_allowed(filename):
    allowed_extensions = ['.html', '.css', '.js', '.php']
    _, ext = os.path.splitext(filename)
    return ext.lower() in allowed_extensions

def procurar_frase(pasta, arquivos_encontrados):
    for nome_arquivo in os.listdir(pasta):
        if os.path.isfile(os.path.join(pasta, nome_arquivo)) and is_file_allowed(nome_arquivo):
            print(f'Lendo o arquivo "{nome_arquivo}" na pasta "{pasta}"...')
            try:
                with open(os.path.join(pasta, nome_arquivo), 'r', encoding='utf-8') as arquivo:
                    conteudo = arquivo.read()
            except UnicodeDecodeError:
                with open(os.path.join(pasta, nome_arquivo), 'r', encoding='latin-1', errors='ignore') as arquivo:
                    conteudo = arquivo.read()
            if re.search(r'Encontro\s+de\s+Negócios', conteudo, re.IGNORECASE):
                arquivos_encontrados.append((nome_arquivo, pasta))

def procurar_em_todas_as_pastas(pasta_principal):
    arquivos_encontrados = []
    for pasta_atual, sub_pastas, _ in os.walk(pasta_principal):
        procurar_frase(pasta_atual, arquivos_encontrados)
    
    for arquivo, pasta in arquivos_encontrados:
        print('------------------------')
        print(f'O arquivo "{arquivo}" na pasta "{pasta}" contém a frase "Encontro de Negócios".')

pasta_principal = '.'

procurar_em_todas_as_pastas(pasta_principal)
