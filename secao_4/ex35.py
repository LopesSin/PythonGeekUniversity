from math import sqrt  # importa o método de raiz quadrada.

cat_a = float(input('Insira o valor do cateto a: '))
cat_b = float(input('Insira o valor do cateto b: '))

hip = sqrt((cat_a ** 2) + (cat_b ** 2))  # onde hip = hipotenusa

print(f'O valor da hipotenusa desse triângulo é {hip:.2f}')
