#1 Olá, Mundo! Escreva um programa queexiba a frase "Olá, mundo!" na tela.
print("Olá, mundo!")

#2 Entrada de Nome Peça ao usuário paradigitar seu nome e exiba a seguinte mensagem: "Seja bem-vindo(a), [nome]!"
nome = input("Digite seu nome: ")
print(f"Seja bem-vindo(a), {nome}!")

#3 Soma de dois números solicite dois números ao usuário e mostre a soma deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é: {soma}")

#4 Maior de dois números Peça dois números ao usuário e exiba qual é o maior deles (ou se são iguais).

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1:
    print(f"O maior número é: {numero2}")
else:
    print("Os números são iguais.")

#5 Conversor de Temperatura Peça uma temperatura em graus Celsius e converta para Fahrenheit, usando a fórmula: F = (C × 9/5) + 32

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")

#6 Calculadora de Média Peça ao usuário três notas e calcule a média. Depois, diga se ele está aprovado (média ≥ 7) ou reprovado.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 7.0:
    print(f"A média é {media}. Você está aprovado(a)!")
else:
    print(f"A média é {media}. Você está reprovado(a).")

#7 Verificador de idade Peça a idade do usuário e diga se ele é:  Menor de idade (< 18)  Maior de idade (≥ 18)
idade = int(input("Digite sua idade: "))

if idade >=18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#8 Mensagem Personalizada Peça o nome do usuário e a cor favorita dele, depois exiba: "Olá [nome], sua cor favorita é [cor]!"

nome_usuario = input("Digite seu nome: ")
cor_favorita = input("Digite sua cor favorita: ")
print(f"Olá {nome_usuario}, sua cor favorita é {cor_favorita}!")

#9 Conversor de Metros para Centímetros e Milímetros Peça um valor em metros e mostre o equivalente em centímetros e milímetros.

metros = float(input("Digite o valor em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"{metros} metros equivalem a {centimetros} centímetros e {milimetros} milímetros.")

#10 Conversor de Moeda Solicite um valor em reais e converta para dólares (use uma taxa fixa que você definir no código).

reais = float(input("Digite o valor em reais: "))
taxa_cambio = 5.0  
dolares = reais / taxa_cambio
print(f"{reais} reais equivalem a {dolares} dólares.")

#11 Ano de Nascimento Peça a idade do usuário e calcule em que ano ele nasceu (considerando que estamos em 2025).

idade_usuario = int(input("Digite sua idade: "))
ano_atual = 2025
ano_nascimento = ano_atual - idade_usuario
print(f"Você nasceu em {ano_nascimento}.")

#12 Verificador de Nota Peça uma nota de 0 a 10 e diga se é insuficiente (< 5), ou boa (≥ 7).

nota_usuario = float(input("Digite uma nota de 0 a 10: "))
if nota_usuario >= 7:
    print("A nota é boa.")
else:
    print("A nota é insuficiente.")

#13 Soma de 3 números Peça três números e mostre a soma total.

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
soma = number1 + number2 + number3
print(f"A soma dos três números é: {soma}")

#14 Saudação Simples Peça o nome do usuário e a cidade onde ele mora, depois exiba: "Olá [nome], você mora em [cidade]!"

name_usuario = input("Digite seu nome: ")
cidade_usuario = input("Digite a cidade onde você mora: ")
print(f"Olá {name_usuario}, você mora em {cidade_usuario}!")

#15 Quadrado e Raiz Solicite um número ao usuário e mostre o quadrado e a raiz quadrada dele.

import math
number = float(input("Digite um número: "))
quadrado = number ** 2
raiz = math.hypot(number, 0)
print(f"O quadrado de {number} é: {quadrado}")
print(f"A raiz quadrada de {number} é: {raiz}")

#16 Cálculo de Idade Peça o ano de nascimento do usuário e calcule a idade que ele terá em 2030.

ano_user_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_2030 = 2030 - ano_user_nascimento
print(f"Em 2030, você terá {idade_em_2030} anos.")

#17 Classificação de Idade Peça a idade do usuário e informe: o Criança (0–12 anos) o Adolescente (13–17 anos) o Adulto (18–59 anos) o Idoso (60 anos ou mais)

idade_user = int(input("Digite sua idade: "))
if idade_user <= 12:
    print("Você é uma criança.")
elif idade_user <= 17:
    print("Você é um adolescente.")
elif idade_user <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

#18 Produto de 3 números Peça três números e mostre o produto total (multiplicação).

num_a = float(input("Digite o primeiro número: "))
num_b = float(input("Digite o segundo número: "))
num_c = float(input("Digite o terceiro número: "))
produto = num_a * num_b * num_c
print(f"O produto dos três números é: {produto}")

# 19 Calculadora de Média Peça duas notas e mostre a média final. Se a média for: o Menor que 5 → "Reprovado" o Entre 5 e 6.9 → "Recuperação" o Maior ou igual a 7 → "Aprovado"

nota_a = float(input("Digite a primeira nota: "))
nota_b = float(input("Digite a segunda nota: "))
media_final = (nota_a + nota_b) / 2
if media_final < 5:
    print(f"A média final é {media_final}. Reprovado.")
elif media_final >= 5 and media_final < 7:
    print(f"A média final é {media_final}. Recuperação.")
elif media_final >= 7:
    print(f"A média final é {media_final}. Aprovado.")
else:
    print("Nota inválida.")

# 20 Par ou Ímpar Peça ao usuário para digitar um número inteiro e informe se ele é par ou ímpar.
numer = int(input("Digite um número inteiro: "))

if numer % 2 == 0:
    print(f"O número {numer} é par.")
else:
    print(f"O número {numer} é ímpar.")

# 21 Cálculo de Desconto Solicite o preço original de um produto e o percentual de desconto (ex: 10 para 10%). Calcule e exiba o valor do desconto e o preço final do produto.
preco_original = float(input("Digite o preço original do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto
print(f"O valor do desconto é: R${valor_desconto}")
print(f"O preço final do produto é: R${preco_final}")

# 22 Calculadora de Área de Retângulo Peça ao usuário a base e a altura de um retângulo e calcule e mostre a sua área.

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = base * altura
print(f"A área do retângulo é: {area}")

# 23 Contador de Caracteres Peça ao usuário para digitar uma palavra ou frase e mostre quantos caracteres ela possui (incluindo espaços).

palavra_ou_frase = input("Digite uma palavra ou frase: ")
quantidade_caracteres = len(palavra_ou_frase)
print(f"A quantidade de caracteres é: {quantidade_caracteres}")

# 24 Tabuada Simples Solicite um número ao usuário e exiba a tabuada de multiplicação desse número, do 1 ao 10.

numero_tabuada = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {numero_tabuada}:")
for i in range(1, 11):
    print(f"{numero_tabuada} x {i} = {numero_tabuada * i}")

# 25 Conversor de Tempo Peça ao usuário um valor em minutos (ex: 150) e converta para o formato de horas e minutos (ex: 2 horas e 30 minutos).

minutos = int(input("Digite um valor em minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")

# 26 Verificador de Número Positivo/Negativo Peça um número e verifique se ele é positivo, negativo ou zero.
numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é zero.")

#27 Cálculo de IMC (Índice de Massa Corporal) Peça ao usuário seu peso (em kg) e sua altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura *altura).

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc}")

#28 Repetidor de Palavras Peça ao usuário uma palavra e um número. Em seguida, exiba a palavra na tela repetida pelo número de vezes informado.


palavra = input("Digite uma palavra: ")
vezes = int(input("Digite o número de vezes que deseja repetir a palavra: "))
for i in range(vezes):
    print(palavra)

# 29 Verificador de Triângulo Peça ao usuário os comprimentos dos três lados de um triângulo e verifique se é possível formar um triângulo com essas medidas. (Dica: a soma de dois lados quaisquer deve ser sempre maior que o terceiro lado).

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("É possível formar um triângulo com essas medidas.")
else:
    print("Não é possível formar um triângulo com essas medidas.")
