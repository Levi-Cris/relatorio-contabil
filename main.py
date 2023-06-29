import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("X:\Arquivos\Vendas")
tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    #print(arquivo) - mostra o nome de todos os arquivos no diretório
    if "Vendas" in arquivo:
        #print(f"D:\Vendas\{arquivo}") - mostra apenas os arquivos de venda do diretório
        tabela = pd.read_csv(f"X:\Arquivos\Vendas\{arquivo}")
        #print(arquivo)
        #print(tabela)
        tabela_total = tabela_total._append(tabela)
#print(tabela_total) - mostra uma única lista com as informações de vendas de todas as lojas

#agrupar produtos de acordo com as vendas:
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_produtos)
print('')
print('-=' * 20)
print('')

#produto com maior faturamento:
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)
print('')
print('-=' * 20)
print('')

#loja que mais vendeu em faturamento:
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_lojas)
print('')
print('-=' * 20)

#gerando gráficos através dos dados:
grafico1 = px.bar(tabela_produtos, x=tabela_produtos.index, y='Quantidade Vendida')
grafico1.show()

grafico2 = px.bar(tabela_faturamento, x=tabela_produtos.index, y='Faturamento')
grafico2.show()

grafico3 = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico3.show()
