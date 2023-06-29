import os
import pandas as pd
import plotly.express as px

def separador_tabela():
    print('')
    print('-=' * 20)
    print('')

lista_arquivo = os.listdir("X:\Arquivos\Vendas")
tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"X:\Arquivos\Vendas\{arquivo}")
        tabela_total = tabela_total._append(tabela)

#agrupar produtos de acordo com o número de vendas:
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_produtos)
separador_tabela()

#produto com maior faturamento:
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)
separador_tabela()

#loja que mais vendeu em faturamento:
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_lojas)
separador_tabela()

#gerando gráficos através dos dados:
grafico1 = px.bar(tabela_produtos, x=tabela_produtos.index, y='Quantidade Vendida')
grafico1.show()

grafico2 = px.bar(tabela_faturamento, x=tabela_produtos.index, y='Faturamento')
grafico2.show()

grafico3 = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico3.show()
