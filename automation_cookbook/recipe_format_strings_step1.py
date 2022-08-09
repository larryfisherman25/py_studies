data = [
    (123456, 10),
    (2000, 17),
    (2500, 170),
    (2500, -170),
]

# Printando o cabeçalho para referência
print('REVENUE | PROFIT | PERCENT')

# Esse modelo alinha e mostra os dados (data) no formato apropriado
TEMPLATE = '{revenue:>7,} | {profit:>+6} | {percent:>7.2%}'

# Printa as linhas de dados
for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent=profit/revenue)
    print(row)
