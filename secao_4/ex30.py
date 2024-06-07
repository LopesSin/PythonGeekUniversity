real = float(input('Insira o valor em Reais: '))
cotacao = float(input('Insira o valor da cotação do dólar: '))

dolar = real / cotacao

print(f'R${real:.2f} são equivalentes a U${dolar:.2f}')
