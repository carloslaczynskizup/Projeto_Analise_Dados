import pandas as pd
import plotly_express as px

# instalar openpyxl
# Análise de dados
dados = pd.read_excel("01_janeiro.xlsx");
print(dados);

# Análises exploratórias
# ver as primeiras linhas
head = dados.head();
print(head);
print();
# ver as últimas linhas
tail = dados.tail();
print(tail);
print();

# total de linhas e colunas
print(dados.shape);
print();

# tipos de dados
print(dados.dtypes);
print();

# Estatísticas
# descreve os dados count, mean, std, min, max, 25%, 50%, 75%.
print(dados.describe());
print();

# Análises
# quantidade de vendas por lojas
print(dados.loja.value_counts());
print();

# quantidade de vendas por tamanho
print(dados.tamanho.value_counts());
print();

# Agrupamento de dados
# quantidade de vendas por tamanho e loja
print(dados.groupby(['loja', 'tamanho']).value_counts());
print();

# quantidade de vendas por loja e forma de pagamento
print(dados.groupby(['loja', 'forma_pagamento']).value_counts());
print();

# Agrupamento de dados por preço
print(dados.groupby('preco').value_counts());
print();

# Agrupamento de dados por loja e soma das vendas por loja
# Faturamento por loja
print(dados.groupby('loja').preco.sum().to_frame());

# Agrupamento de dados por loja e soma das vendas por loja
# Faturamento médio por loja
print(dados.groupby('loja').preco.mean().to_frame());
print();

# Agrupar por mais de uma coluna
# Faturamento por loja e forma de pagamento
print(dados.groupby(['loja', 'forma_pagamento']).preco.sum().to_frame());
print();

# Agrupar por mais de uma coluna
# Faturamento forma de pagamento e estado
print(dados.groupby(['forma_pagamento', 'estado']).preco.sum().to_frame());
print();

# Agrupar por mais de uma coluna
# Faturamento por Loja e estado
print(dados.groupby(['loja', 'estado']).preco.sum().to_frame());
print();

# Agrupar por mais de uma coluna
# Faturamento por Loja e estado
# e gerar em arquivo excel
print(dados.groupby(['loja', 'estado']).preco.sum().to_excel("faturamento.xlsx"));
print();

# Criando gráficos e Visualizações de dados
# instalar a biblioteca plotly_express
# gerar gráficos e históricos
print(px.histogram(dados, x="loja", text_auto=True));
print();

# gerar loja e preço
print(px.histogram(dados, x="loja", y="preco", text_auto=True));
print();

# gerar loja e preço e forma de pagamento
print(px.histogram(dados, x="loja", y="preco", color="forma_pagamento", text_auto=True));
print();

# Estruturas de repetição
# Estrutura de dados - LISTA
# nomes = ["Ana", "João", "Maria", "Pedro", "Paula"];
# type(nomes);
#
# # Looping for
# for nome in nomes:
# 	print(nome);
colunas = ["loja", "tamanho", "preco", "forma_pagamento"];
for coluna in colunas:  # gerar vários gráficos
	grafico = px.histogram(dados, x=coluna, y="preco", color="forma_pagamento", text_auto=True);
	grafico.show();

# Gerar Gráfico animado em html, tipo storytelling do faturamento por loja e vendas durante um ano.







