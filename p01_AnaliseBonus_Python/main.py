# Passo a passo da solução

# instalar:
# pandas - integração com o excel e o python (digitar no terminal o comando pip install pandas)
# openyxl - integração com o excel e o python (digitar no terminal o comando pip install openyxl)
# twilio - integração com o sms e o Python (digitar no terminal o comando pip install twilio)

from twilio.rest import Client
import pandas as pd

# Your Account SID from twilio.com/console ---ENVIO DE SMS PELO TWILIO
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""
client = Client(account_sid, auth_token)

# 1. abrir o arquivo do excel
lista_meses = ['01_janeiro', '02_fevereiro', '03_marco', '04_abril', '05_maio', '06_junho']

for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
# 2. Para cada arquivo, verificar se algum valor na coluna de vendas é maior do que 55.000
    if (tabela_vendas['Vendas'] > 55000).any(): #se qualquer valor na coluna for maior que 55.000
        #quem é o vendedor e quantos vendeu?
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês {mes} encontrado Vendas com Valor maior que 55.000')
        print(f'No mês {mes} quem alcançou a meta foi o Vendedor: {vendedor} com Vendas: {vendas}')
        print('---------------------------------')
# 3. Se algum valor for maior que 55.000, envia um SMS.
        message = client.messages.create(
            to="",
            from_="",
            #body=f'No mês {mes} quem alcançou a meta foi o Vendedor: {vendedor} com Vendas: {vendas}')
            body='Vou desligar e tentar fazer macarrão - Hahaha!')
        print(message.sid)
