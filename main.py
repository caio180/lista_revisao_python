# Cadastro de usuário
print("Cadastro de usuário")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cidade = str(input("Digite sua cidade: "))

print(f"\nNome: {nome} \nIdade: {idade} \nCidade: {cidade}")

# Conversor de temperatura

print("Conversor de temperatura")

escala = input(" Escolha o tipo de escala Termométrica = ").strip().lower()

if escala == "1":
    tcf = float(input("Temperatura em celsius = "))
    tempcf = (tcf * 9/5 ) + 32
    print(round(tempcf, 2), " °F.")
else:
    print("Erro, digite uma temperatura válida")

# Calculadora de tempo

print("Calculadora de tempo")

minutos = int(input("Digite o valor em minutos: "))

print(f"Conversão de minutos para horas: {minutos / 60}")

# Divisão de valores

print("Divisão de valores")


num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num2 != 0:
    print(f"Resultado da divisão: {num1 / num2} \nQuociente inteiro: {num1 // num2} \nResto da divisão: {num1 % num2}")
else:
    print("Error, denominador não pode ser zero")

# Ingresso de cinema

print("Ingresso de cinema: ")

idade_usuario = int(input("Digite sua idade: "))


if idade_usuario < 12:
    print("Valor do ingresso: R$ 10,00")
elif idade_usuario >=12 and idade_usuario <=17:
    print("Valor do ingresso: R$ 15,00")
elif idade_usuario >=18:
    print("Valor do ingresso: R$ 25,00")

# Contagem Personalizada

print("Contagem Personalizada")

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

for i in range(numero1, numero2):
    print(i)

# Análise de números

print("Análise de números")


number1 = int(input("Digite o primeiro numero: "))
number2 = int(input("Digite o segundo numero: "))
number3 = int(input("Digite o terceiro numero: "))
number4 = int(input("Digite o quarto numero: "))
number5 = int(input("Digite o quinto numero: "))


numeros = [number1, number2, number3, number4, number5]

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)


print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma dos números: {soma}")
print(f"Média: {media}")

# Verificador de senha


print("Verificador de senha")


senha = input("Digite sua senha").strip()
senhaC = "python123"


if senha.lower() == senhaC:
    print("Acesso permitido")
else:
    print("Senha incorreta")


# Sistema de votação

candidatos = {
    1: "Henrique",
    2: "Camila",
    3: "Reginaldo"
}


votos = {
    1: 0,
    2: 0,
    3: 0
}
votos_nulos = 0


print(" Sistema de Votação ")


while True:
    print("\nCandidatos disponíveis:")
    for numero, nome in candidatos.items():
        print(f"  [{numero}] {nome}")
    print("  [0] Encerrar votação")


    try:
        escolha = int(input("\nDigite o número do seu candidato: "))
    except ValueError:
        print("Erro: Por favor, digite apenas números.")
        continue

    if escolha == 0:
        print("\nEncerrando a votação...")
        break
    elif escolha in candidatos:
        votos[escolha] += 1
        print(f"Voto confirmado para {candidatos[escolha]}!")
    else:
        votos_nulos += 1
        print("Número inválido! Voto computado como NULO.")


print("\n Resultado Final ")
for numero, nome in candidatos.items():
    print(f"{nome}: {votos[numero]} voto(s)")

print(f"Votos Nulos: {votos_nulos}")

# Controle de compras

produtos = {}


for i in range(5):
  nome = input(f"Nome do {i + 1}º produto: ")
  preco = float(input("Preço: R$ "))
  produtos[nome] = preco

total = sum(produtos.values())
media = total / 5
mais_caro = max(produtos, key=produtos.get)

print("\nResumo:")
print("Produtos cadastrados:", produtos)
print(f"Valor total: R$ {total}")
print(f"Mais caro: {mais_caro} (R$ {produtos[mais_caro]})")
print(f"Média: R$ {media}")
