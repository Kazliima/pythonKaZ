import os
os.system("cls")
os.system("color 3")

# Continuação Input com Int e Float
 #int() -> converte para inteiro
 #float() -> converte para n quebrado

# numero = 10
# numero2 = input("digite um numero: ")
# print("o tipo do numero é", type(numero2))
# soma = numero + int(numero2)
# print(f"soma de {numero} + {numero2} = ", soma)

#exemplo2
# num1 = input("digite um numero: ")
# soma = float(num1) = 15
# print("A soma de ",num1 , "+", "15" ,"=", soma)

# exemplo3
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))
# soma = n1+n2
# print(f"a soma de {n1} + {n2} = ", soma)


#desafio 1
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))
# multiplicacao = n1*n2
# print(f"a soma de {n1} + {n2} = ", multiplicacao)


#desafio 2 
# n1 = float(input("digite um numero: "))
# adicao =(n1+(1))
# subtracao =(n1-(1))
# print(f"seu sucessor é", adicao)
# print(f"seu antecessor é", subtracao)


#desafio 3
# nascimento = int(input("digite o ano em que voce nasceu: "))
# atual = int(2025)
# idade = atual-nascimento
# print(f"voce tem ", idade,"anos")

#porcentagem
# print("25% de 100= ", 0.25 * 100)
# print("4% de 100= ", 0.04 * 400)
# print("99% de 100= ", 0.99 * 1525)

# supondo que um produto custa 150 reais
# e o caixa deu um desconto de 15%
# exemplo = float(input("digite o preco do produto: "))
# desconto = 0.15 * exemplo
# print("o preço do produto de 15% de desconto é", exemplo-desconto)


# print(">"*17,"PAGUE MAIS LEVE MENOS","<"*17)
# produto1 = input("Digite o nome do 1 produto: ")
# valor1 = float(input("Digite seu valor: "))
# produto2 = input("Digite o nome do 2 produto: ")
# valor2 = float(input("Digite seu valor: "))
# desconto1 = 0.10 * valor1
# desconto2 = 0.25 * valor2
# total = (valor1-desconto1)+(valor2-desconto2)
# print("="*15,"LAVA-CA$H","="*15)
# print(produto1, "custa", valor1, "com 10% de desconto =", valor1-desconto1)
# print(produto2, "custa", valor2, "com 25% de desconto =", valor2-desconto2)

# print(f"TOTAL R$: {valor1-desconto1} + {valor2-desconto2} = ", round(total))

rounded_number = round(53.7932213213188, 4)
print(rounded_number)


