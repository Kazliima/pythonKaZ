import os
os.system("cls")


#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
# SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
#match valor:
#   case valor:


# linguagem = 100

# match linguagem:

#     case "python":
#         print(" é facil")
#     case "java":
#         print(" muito codigo , python faz com linhas menores")
#     case "c#":
#         print(" massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauan nao dorme")
#     case 10:
#         print("entrou aqui !")
#     case _ :
#         print("outro caso")


#ATIVIDADE 1
# dia = input("digite o numero do dia da semana: ")

# match dia:

#     case "1":
#         print("domingo")
#     case "2":
#         print("segunda")
#     case "3":
#         print(" terça")
#     case "4":
#         print("quarta")
#     case "5":
#         print("quinta")
#     case "6":
#         print("sexta")
#     case "7":
#         print("sabado")


#ATIVIDADE 2

# print ( "="*15,"LOJA DO CHINA","="*15,"\n")
# print ("="*15,"OPÇÕES DE CELULARES","="*15,"\n")

# print ("""
# 1 = XIAOMI -> R$2000,00
# 2 = IPHONE -> R$3000,00
# 3 = SAMSUNG -> R$5000,00
#        \n""")

# print ("="*15,"OPÇÕES DE FRETE","="*15,"\n")
# print ("""
# 1 = SC -> R$10,00
# 2 = MG -> R$15,00
# 3 = SP -> R$20,00
#        \n""")

# cel = int(input("Digite o número do celular que você deseja: "))
# frete = int(input("Digite o número do frete: "))

# match cel:
#     case 1:
#         preço = 2000
#     case 2:
#         preço = 3000
#     case 3:
#         preço = 5000

# match frete:
#     case 1:
#         frete = 10
#     case 2:
#         frete = 15
#     case 3:
#         frete = 20

# print ("*"*40, "\n")
# print (f"PREÇO R$: {preço}")
# print (f"FRETE R$: {frete} ")
# print (f"TOTAL R$: {preço + frete}")



# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50"


# import random

# pedra = 1
# papel = 2
# tesoura = 3
# jogo = int(input("escolha:\n 1=pedra\n 2=papel\n 3=tesoura\n"))


# jogo = random.randint(1,3)


# match eu:

#      case _ if papel <3 : 
#         print("perdeu")
#      case _ if papel ==2:
#          print("empatou")
#      case _ if papel > 1:
#          print("ganhou")

# match robo:

#      case _ if tesoura <3 : 
#         print("perdeu")
#      case _ if tesoura ==2:
#          print("empatou")
#      case _ if tesoura > 1:
#          print("ganhou")




import random

def escolha_computador():
    return random.choice(['pedra', 'papel', 'tesoura'])

def jogar():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    print("Escolha entre 'pedra', 'papel' ou 'tesoura'.")

    usuario = input("Sua escolha: ").lower()

    if usuario not in ['pedra', 'papel', 'tesoura']:
        print("Escolha inválida! Por favor, escolha 'pedra', 'papel' ou 'tesoura'.")
        return

    pc = escolha_computador()
    print(f"Computador escolheu: {pc}")

    match (usuario, pc):
        case ('pedra', 'pedra') | ('papel', 'papel') | ('tesoura', 'tesoura'):
            print("Empate!")
        case ('pedra', 'tesoura') | ('papel', 'pedra') | ('tesoura', 'papel'):
            print("Você venceu!")
        case _:
            print("Você perdeu!")

jogar()
