dias = int(input('Insira a quantidade de dias trabalhados: '))

valor_bruto = 30.0 * dias  # 30 reais o dia
valor_liquido = valor_bruto * 0.92  # 8% de imposto

print(f'O valor liquido a ser recebido é de R${valor_liquido}')
