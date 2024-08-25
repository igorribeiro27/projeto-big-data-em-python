# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar e processar os dados
def carregar_dados(caminho_arquivo):
    try:
        dados = pd.read_csv(caminho_arquivo)
        return dados
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho.")
        return None

# Função para visualizar a distribuição de uma variável
def visualizar_distribuicao(dados, coluna):
    plt.figure(figsize=(10, 6))
    sns.histplot(dados[coluna], kde=True)
    plt.title(f'Distribuição de {coluna}')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.show()

# Função para visualizar a relação entre duas variáveis
def visualizar_relacao(dados, coluna1, coluna2):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=dados, x=coluna1, y=coluna2)
    plt.title(f'Relação entre {coluna1} e {coluna2}')
    plt.xlabel(coluna1)
    plt.ylabel(coluna2)
    plt.show()

# Função principal
def main():
    caminho_arquivo = 'dados_comunitarios.csv'  # Substitua pelo caminho real do arquivo
    dados = carregar_dados(caminho_arquivo)
    
    if dados is not None:
        # Exemplo de visualização da distribuição de uma coluna
        visualizar_distribuicao(dados, 'renda')
        
        # Exemplo de visualização da relação entre duas colunas
        visualizar_relacao(dados, 'idade', 'renda')

# Execução do script
if __name__ == '__main__':
    main()
