import os

def renomear_arquivos(diretorio, prefixo="", sufixo=""):
    try:
        # Mudar para o diretório especificado
        os.chdir(diretorio)
        arquivos = os.listdir(diretorio)
        
        for arquivo in arquivos:
            # Ignorar pastas no diretório
            if os.path.isfile(arquivo):
                nome, extensao = os.path.splitext(arquivo)
                novo_nome = f"{prefixo}{nome}{sufixo}{extensao}"
                os.rename(arquivo, novo_nome)
                print(f"Renomeado: {arquivo} -> {novo_nome}")
        
        print("\nRenomeação concluída!")
    except Exception as e:
        print(f"Erro ao renomear arquivos: {e}")

# Configurações
diretorio = input("Digite o caminho do diretório com os arquivos: ")
prefixo = input("Digite o prefixo (opcional): ")
sufixo = input("Digite o sufixo (opcional): ")

# Chamar a função
renomear_arquivos(diretorio, prefixo, sufixo)