# Sistema de Orçamentos para uma consultoria.

# Sistema básico de impressão em PDF. Ainda falta o template.

from fpdf import FPDF

# Mostrando dados para o usuário
print("Olá, como você está hoje?");
print();
print("Orçamento gerado com sucesso!");
# Entrada de dados do usuário
# input("Digite a descrição do Projeto: ");
# input("Digite a quantidade de horas previstas: ");
# input("Digite o valor da hora trabalhada: ");
# input("Digite o prazo: ");

# Armazenar os dados com variáveis
projeto = input("Digite a Descrição do Projeto: ");
horasPrevistas = input("Digite a Quantidade de horas previstas: ");
valorHora = input("Digite o Valor da hora trabalhada: ");
prazo = input("Digite o Prazo: ");
print();

# Mostrar os dados do cálculo do orçamento do projeto
valorTotal = float(horasPrevistas) * float(valorHora);
print("O valor total do projeto é: {:.2f} reais".format(valorTotal));

# Gerando o PDF do Orçamento
# pip install fpdf (atentar ao import: from fpdf import FPDF)
pdf = FPDF();
pdf.add_page();
pdf.set_font('Arial', 'B', 14);

pdf.text(100, 120, "Nome do Projeto: " + projeto);
pdf.text(100, 135, "Quantidade de horas previstas: " + horasPrevistas);
pdf.text(100, 150, "Valor da hora trabalhada: " + valorHora);
pdf.text(100, 165,  "Prazo: " + prazo);
pdf.text(100, 185,  "Valor total do projeto: R$ " + str(valorTotal));


pdf.output("Orçamento.pdf");

print("PDF - Orçamento gerado com sucesso!");
