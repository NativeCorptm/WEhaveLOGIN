import os
import time
from tqdm import tqdm
import urllib.parse

def buscar_e_escrever_linhas_com_palavra_chave(nome_arquivo, palavra_chave):
    linhas_relevantes = []
    erros_decodificacao = 0
    with open(nome_arquivo, 'rb') as arquivo:
        for linha_bytes in arquivo:
            try:
                linha = linha_bytes.decode('utf-8')
                if palavra_chave in linha:
                    linhas_relevantes.append(linha.strip())
            except UnicodeDecodeError:
                erros_decodificacao += 1
    return linhas_relevantes, erros_decodificacao

def limpar_nome_arquivo(nome_arquivo):
    caracteres_invalidos = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in caracteres_invalidos:
        nome_arquivo = nome_arquivo.replace(char, '_')
    return nome_arquivo

print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ")
def main():

    print(" " * 50000 + "\u001b[92m               WEhaveLOGIN\u001b[0m");
    print(" " * 500)
    pasta_db = ("/sdcard/WEhaveLOGIN")
    
    if not os.path.isdir(pasta_db):
        print(f"\u001b[35m The command '{pasta_db}' does not exist\u001b[0m")
        return

    palavra_chave = input("\u001b[35m Type the site or URL:\u001b[0m");print(" " * 50000)
    palavra_chave_encoded = urllib.parse.quote(palavra_chave)

    nome_arquivo_saida = f" {limpar_nome_arquivo(palavra_chave_encoded)}.txt"

    arquivos_txt = [arquivo for arquivo in os.listdir(pasta_db) if arquivo.endswith('.txt')]

    if not arquivos_txt:
        print(f"\u001b[35mWe found nothing '{pasta_db}'.\u001b[0m")
        return
        
 
    with tqdm(total=len(arquivos_txt), desc="") as progresso_barra:
        total_linhas_encontradas = 0
        total_erros_decodificacao = 0
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            for arquivo_txt in arquivos_txt:
                caminho_arquivo = os.path.join(pasta_db, arquivo_txt)
                linhas_relevantes, erros_decodificacao = buscar_e_escrever_linhas_com_palavra_chave(caminho_arquivo, palavra_chave)
                total_linhas_encontradas += len(linhas_relevantes)
                total_erros_decodificacao += erros_decodificacao                
                if linhas_relevantes:
                    arquivo_saida.write(f"\n")
                    arquivo_saida.writelines("\n".join(linhas_relevantes))
                    arquivo_saida.write("\n\n")
                progresso_barra.update(1)
                time.sleep(0.1)

    if total_linhas_encontradas == 0:
        print("\u001b[35mWe didn't find anything.\u001b[0m")
    else:
        print(f"\u001b[35mLogins found: {total_linhas_encontradas}, you will find it on your folder\u001b[0m")

if __name__ == "__main__":
    main()

