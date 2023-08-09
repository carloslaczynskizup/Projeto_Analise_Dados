# Automatizar uma tarefa para finanças
# Automatizar pesquisas de uma determinada bolsa de valores e suas movimentações
# observação: PYPI site de Encontre, instale e publique pacotes Python com o Python Package Index.

import yfinance as yf;  # as yf coloca apelido na biblioteca
import matplotlib.pyplot as plt  # as plt coloca apelido na biblioteca
import pyautogui as pya;

# Instalar e importar as bibliotecas: pip install yfinance
# pip install matplotlib (plotar gráficos)
# pip install pyautogui (automatizar)

# Passo 1 - buscar as informações da bolsa de forma automática

dados = yf.Ticker("TAEE11.SA").history("6mo");
fechamento = dados.Close;
print(fechamento);  # busca a coluna de fechamento da bolsa
fechamento.plot();
plt.title("Preços de Fechamento da Ação - TAEE11.SA")
plt.xlabel("Data")
plt.ylabel("Preço de Fechamento")
plt.show()

# Passo 2 - criar as análises dos dados
maxima = round(fechamento.max(), 2);  # arredonda o valor
minima = round(fechamento.min(), 2);
atual = round(fechamento.iloc[-1], 2);  # indice -1 é o último valor, ou seja a última linha.
atual1 = fechamento[-1];
print(maxima);  # valor máximo da coluna de fechamento
print(minima);  # valor mínimo da coluna de fechamento
print(atual);  # valor atual da coluna de fechamento
print(atual1);  # valor atual da coluna de fechamento
print();
print("A cotação atual é: R$", atual);
print("A cotação mínima é: R$", minima);
print("A cotação máxima é: R$", maxima);

# Passo 3 - criar os relatórios ou enviar um email com os resultados.
# abrir nova janela do navegador
# digitar o endereço do email destinatário
# clicar no botão escrever

