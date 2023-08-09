# Automatizar uma tarefa para finanças
# Automatizar pesquisas de uma determinada bolsa de valores e suas movimentações
# observação: PYPI site de Encontre, instale e publique pacotes Python com o Python Package Index.

import yfinance as yf;  # as yf coloca apelido na biblioteca
import matplotlib.pyplot as plt;  # as plt coloca apelido na biblioteca
import pyautogui as pya;
import pyperclip as pyc;
import time;
import webbrowser; #abre o navegador padrão do sistema

# Instalar e importar as bibliotecas: pip install yfinance
# pip install matplotlib (plotar gráficos)
# pip install pyautogui (automatizar)
# pip install pyperclip (automatizar o processo de copiar e colar)

# Passo 1 - buscar as informações da bolsa de forma automática
ticker = input("Digite o código da ação: "); #exemplo: TAEE11.SA
dados = yf.Ticker(ticker).history("6mo");
fechamento = dados.Close;
print(fechamento);  # busca a coluna de fechamento da bolsa
fechamento.plot();
time.sleep(2);
plt.title("Preços de Fechamento da Ação - " + ticker);
plt.xlabel("Data");
plt.ylabel("Preço de Fechamento");
plt.show(); #abaixo pode colocar implementação para salvar a plotagem gerada.
time.sleep(2);
# pya.hotkey("alt", "f4");
# time.sleep(2);


# Passo 2 - criar as análises dos dados no console
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

# Passo 3 - criar os relatórios ou enviar um email com os resultados. AUTOMAÇÃO
# 1. abrir nova janela do navegador (Ctrl + t)
# 2. digitar o endereço do servidor de email
# 3. digitar o endereço do email destinatário
url = "https://mail.google.com/mail/u/0/#inbox";
webbrowser.open(url); # aqui abre o navegador padrão do sistema
time.sleep(8); #ou ode usar o pyautogui.PAUSE = 2
# pya.hotkey("ctrl", "t");

# 4. clicar no botão escrever
# posicao = pya.position(); aqui foi uma sacada para pegar o valor da posição
# print(posicao); aqui foi uma sacada para pegar o valor da posição no console do IntelliJ
pya.click(191, 294);
time.sleep(2);

# 5. Digitar o destinatário do email e assunto
pya.write("l5b6F@example.com");
time.sleep(2);
pya.hotkey("enter");
pya.hotkey("tab");
time.sleep(2);
#Assunto de e-mail
pya.write("Teste Automatizado");
time.sleep(2);
pya.hotkey("tab");
time.sleep(2);

# 6. Digitar o conteúdo do email
#pya.write("Segue em anexo o relatório de análise dos dados"); pode ser usado o pyperclip.copy para copiar e colar
#f antes das aspas triplas para formatar o texto de acordo com a análise em questão.
mensagem = f"""
Segue abaixo o relatório de análise dos dados.

Sendo o seguinte da ação {ticker}:

Cotação mínima: R$ {minima}
Cotação máxima: R$ {maxima}
Cotação atual: R$ {atual}


Qualquer dúvida estou a disposição.

Atenciosamente,

Carlos.
""";
time.sleep(2);
pyc.copy(mensagem);
time.sleep(2);
pya.hotkey("ctrl", "v");

# pyc.copy("Segue abaixo o relatório de análise dos dados.");
# pya.hotkey("ctrl", "v");
# time.sleep(1);
# pya.hotkey("enter");
# pya.hotkey("enter");
# pyc.copy("Atenciosamente,");
# pya.hotkey("ctrl", "v");
# pya.hotkey("enter");
# pyc.copy("Carlos.");
# pya.hotkey("ctrl", "v");
time.sleep(1);
pya.hotkey("tab");
time.sleep(1);
pya.hotkey("enter");

exit();


