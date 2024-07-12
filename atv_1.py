#1. Calculadora Simples: Solicite ao usuário para inserir dois valores numéricos,
#realize as operações de soma, subtração, multiplicação e divisão, e ao final exiba
#os valores de cada uma das operações.

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
soma = num1+num2
mult = num1*num2
sub = num1-num2
divis = num1/num2

print('O resultado da soma é:',soma)
print('O resultado da multiplicação é:',mult)
print('O resultado subtração é:',sub)
print('O resultado divisão é:',divis)
print('Fim do Programa')

#2. Conversor de Temperatura: Solicite ao usuário um valor de temperatura em graus
#Celsius, converta-a para Fahrenheit e exiba o resultado da conversão.

temp = int(input('Digite a temperatura em ºC: '))
conv = (temp * 1.8) + 32
print('A temperatura em Fahrenheit será:', conv)
print('Fim do Programa')

#3. Área do Círculo: Solicite ao usuário um valor do raio de um círculo, calcule sua
#área e exiba o resultado do cálculo.

r = int(input('Digite o valor do raio do círculo: '))
A = 