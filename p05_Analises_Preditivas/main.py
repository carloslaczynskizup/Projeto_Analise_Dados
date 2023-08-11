import yfinance as yf;  # as yf coloca apelido na biblioteca
from prophet import Prophet;
from prophet.plot import plot_plotly;
import plotly.graph_objects as go;


ticker = input("Digite o código da ação para análise: ");  # exemplo: TAEE11.SA
dados = yf.Ticker(ticker).history("2y");

# print(dados.head());
# print(dados.tail());

# Tratando os dados
# resetando o índice da tabela
treinamento = dados.reset_index();  # resetar o índice
treinamento = treinamento[["Date", "Close"]]
treinamento["Date"] = treinamento["Date"].dt.date;
treinamento.columns = ["ds", "y"];  # renomear nomes das colunas
print(treinamento);

# Criando e treinando o modelo de Machine Learning
# instalar a biblioteca prophet - pip install prophet no PowerShell
modelo = Prophet();

# treinar o modelo
modelo.fit(treinamento);

# Criar o período de previsão
# passo 1 - criar o período de previsão
# a biblioteca abaixo cria o período de previsão
periodo = modelo.make_future_dataframe(90);  # 90 meses

# Criando as nossas previsões
previsoes = modelo.predict(periodo);
print(previsoes);

# Plotando as previsões
plotagem = plot_plotly(modelo, previsoes);
fig = go.Figure(data=plotagem);
fig.add_trace(go.Scatter(x=previsoes.ds, y=previsoes.yhat));

fig.write_html("previsao.html");
fig.write_image("previsao.png");






